"""Retrieval components.

CPU:  BM25 (own sparse implementation), document-number boosting, Reciprocal Rank Fusion, MMR.
GPU:  dense retrieval with FAISS and cross-encoder reranking live in `src/dense.py` (needs torch).

All retrievers return a list of (chunk_idx, score) sorted by score desc, where chunk_idx is the
row index in the chunk file (== chunk_id).
"""
import json
import re
import unicodedata
import zlib
from pathlib import Path

import numpy as np

from .legal_text import find_doc_ids, normalize_doc_id

# Very common Vietnamese function words; removing them helps BM25 on long legal questions
STOPWORDS = set("""và của các có cho là được trong theo với về những này đó khi thì để tại từ một như
bị đã sẽ không cũng hay hoặc nào gì ra sao thế phải nếu đến trên dưới hơn nhưng vì do bởi mà còn
đang rất nhiều ít lại vào sau trước bao quy định""".split())


def load_chunks(path, fields=("chunk_id", "file", "doc_id", "doc_id_norm", "year", "doc_type", "status", "header", "dieu", "text")):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            rows.append({k: d.get(k) for k in fields})
    return rows


def chunk_to_index_text(c):
    """Text that gets indexed / embedded for a chunk (header gives document context)."""
    return (c["header"] + "\n" + c["text"]) if c.get("header") else c["text"]


# ------------------------------------------------------------------ tokenisation
_tok_re = re.compile(r"\w+", re.UNICODE)


def tokenize(text, word_segment=False, remove_stopwords=True):
    """Syllable tokens (default) or pyvi word-segmented tokens (`word_segment=True`, slower)."""
    text = unicodedata.normalize("NFC", text).lower()
    if word_segment:
        from pyvi import ViTokenizer
        text = ViTokenizer.tokenize(text)
    toks = _tok_re.findall(text)
    if remove_stopwords:
        toks = [t for t in toks if t not in STOPWORDS]
    return toks


def tokenize_with_bigrams(text, **kw):
    """Syllables + adjacent syllable bigrams: a cheap approximation of Vietnamese words."""
    t = tokenize(text, **kw)
    return t + [a + "_" + b for a, b in zip(t, t[1:])]


# ------------------------------------------------------------------ BM25
def _h(tok, n_buckets):
    return zlib.crc32(tok.encode("utf-8")) % n_buckets


class BM25Retriever:
    """Memory-efficient BM25 (Okapi) on a scipy sparse matrix with the hashing trick.

    Tokens are hashed into `n_buckets` columns (stable crc32), so no vocabulary has to be kept in RAM.
    The document-term matrix stores the final BM25 weight of every (chunk, term) pair, and a query
    score is simply the sum of the query-term columns.
    """

    def __init__(self, k1=1.2, b=0.75, bigrams=True, word_segment=False, n_buckets=1 << 24):
        self.k1, self.b, self.bigrams, self.word_segment, self.n_buckets = k1, b, bigrams, word_segment, n_buckets
        self.M = None  # CSC matrix (n_docs x n_buckets)

    def _tok(self, text):
        f = tokenize_with_bigrams if self.bigrams else tokenize
        return f(text, word_segment=self.word_segment)

    def fit(self, texts, show_progress=True):
        from array import array
        from collections import Counter
        import scipy.sparse as sp
        from tqdm import tqdm
        indptr, indices, tfs, dls = array("q", [0]), array("i"), array("f"), array("f")
        it = tqdm(texts, desc="BM25 tokenising", mininterval=10) if show_progress else texts
        for t in it:
            toks = self._tok(t)
            cnt = Counter(_h(x, self.n_buckets) for x in toks)
            indices.extend(cnt.keys())
            tfs.extend(cnt.values())
            indptr.append(len(indices))
            dls.append(len(toks))
        n = len(dls)
        indptr = np.frombuffer(indptr, dtype=np.int64)
        indices = np.frombuffer(indices, dtype=np.int32)
        tf = np.frombuffer(tfs, dtype=np.float32).copy()
        dl = np.frombuffer(dls, dtype=np.float32)
        df = np.bincount(indices, minlength=self.n_buckets).astype(np.float32)
        idf = np.log(1 + (n - df + 0.5) / (df + 0.5)).astype(np.float32)
        row_dl = np.repeat(dl, np.diff(indptr))
        norm = self.k1 * (1 - self.b + self.b * row_dl / dl.mean())
        tf = idf[indices] * tf * (self.k1 + 1) / (tf + norm)
        del row_dl, norm
        self.M = sp.csr_matrix((tf, indices, indptr), shape=(n, self.n_buckets)).tocsc()
        return self

    def scores(self, query):
        q = self._tok(query)
        if not q:
            return None
        cols = sorted(set(_h(x, self.n_buckets) for x in q))
        return np.asarray(self.M[:, cols].sum(axis=1)).ravel()

    def search(self, query, k=20, restrict=None):
        s = self.scores(query)
        if s is None:
            return []
        if restrict is not None:          # only score inside a subset of chunk indices
            restrict = np.asarray(restrict)
            sub = s[restrict]
            top = np.argsort(-sub)[:k]
            return [(int(restrict[i]), float(sub[i])) for i in top]
        k = min(k, len(s))
        top = np.argpartition(-s, k - 1)[:k]
        top = top[np.argsort(-s[top])]
        return [(int(i), float(s[i])) for i in top]

    def save(self, path):
        import scipy.sparse as sp
        Path(path).mkdir(parents=True, exist_ok=True)
        sp.save_npz(Path(path, "bm25.npz"), self.M, compressed=False)
        Path(path, "cfg.json").write_text(json.dumps({"k1": self.k1, "b": self.b, "bigrams": self.bigrams,
                                                      "word_segment": self.word_segment, "n_buckets": self.n_buckets}))

    @classmethod
    def load(cls, path):
        import scipy.sparse as sp
        cfg = json.loads(Path(path, "cfg.json").read_text())
        r = cls(**cfg)
        r.M = sp.load_npz(Path(path, "bm25.npz")).tocsc()
        return r


# ------------------------------------------------------------------ doc-number boosting
class DocIdIndex:
    """Maps a normalised document number to the chunk indices of that document."""

    def __init__(self, chunks):
        self.by_id = {}
        for i, c in enumerate(chunks):
            for key in {c["doc_id_norm"], normalize_doc_id(c["doc_id"] or "")}:
                if key:
                    self.by_id.setdefault(key, []).append(i)

    def chunks_for_question(self, question):
        ids = find_doc_ids(question)
        hits = []
        for d in ids:
            hits.extend(self.by_id.get(d, []))
        return ids, hits


def doc_id_rerank(ranked, question, doc_index, chunks, bonus=1.0):
    """Move chunks of a document whose number is written in the question to the top."""
    ids, hits = doc_index.chunks_for_question(question)
    if not hits:
        return ranked
    hit = set(hits)
    return sorted(ranked, key=lambda x: (x[0] in hit, x[1]), reverse=True)


# ------------------------------------------------------------------ fusion / diversity
def rrf(rank_lists, k=60, weights=None, top_n=None):
    """Reciprocal Rank Fusion of several [(idx, score)] lists."""
    weights = weights or [1.0] * len(rank_lists)
    acc = {}
    for w, lst in zip(weights, rank_lists):
        for r, (idx, _) in enumerate(lst):
            acc[idx] = acc.get(idx, 0.0) + w / (k + r + 1)
    out = sorted(acc.items(), key=lambda x: x[1], reverse=True)
    return out[:top_n] if top_n else out


def mmr(query_vec, cand_vecs, cand_ids, k=5, lam=0.7):
    """Maximal Marginal Relevance on normalised vectors. Returns selected ids."""
    q = query_vec / (np.linalg.norm(query_vec) + 1e-12)
    V = cand_vecs / (np.linalg.norm(cand_vecs, axis=1, keepdims=True) + 1e-12)
    rel = V @ q
    selected, rest = [], list(range(len(cand_ids)))
    while rest and len(selected) < k:
        if not selected:
            j = int(np.argmax(rel[rest]))
        else:
            div = (V[rest] @ V[selected].T).max(1)
            j = int(np.argmax(lam * rel[rest] - (1 - lam) * div))
        selected.append(rest.pop(j))
    return [cand_ids[i] for i in selected]


def dedup_by_text(ranked, chunks, max_per_doc=3):
    """Drop near-identical chunks (same doc + same first 200 chars) and cap chunks per document."""
    seen, per_doc, out = set(), {}, []
    for idx, s in ranked:
        c = chunks[idx]
        key = (c["file"], c["text"][:200])
        if key in seen or per_doc.get(c["file"], 0) >= max_per_doc:
            continue
        seen.add(key)
        per_doc[c["file"]] = per_doc.get(c["file"], 0) + 1
        out.append((idx, s))
    return out
