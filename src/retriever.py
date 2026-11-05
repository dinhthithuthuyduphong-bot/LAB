"""One configurable retriever used by evaluation, generation and the demo.

mode:
  "bm25"          BM25 only (CPU)
  "dense"         FAISS only (GPU recommended)
  "hybrid"        BM25 + dense fused with RRF
options:
  doc_id_boost    if the question writes a document number that exists in the corpus, search inside it first
  rerank          cross-encoder rerank of the fused candidates (GPU recommended)
"""
from dataclasses import dataclass

from . import config
from .retrieval import BM25Retriever, DocIdIndex, dedup_by_text, load_chunks, rrf, chunk_to_index_text


@dataclass
class RetrieverConfig:
    chunks: str = "legal"
    mode: str = "bm25"
    bm25_variant: str = ""
    dense_model: str = config.EMBEDDING_MODEL
    doc_id_boost: bool = True
    rerank: bool = False
    reranker_model: str = config.RERANKER_MODEL
    candidates: int = config.RETRIEVE_K
    top_k: int = config.TOP_K
    max_per_doc: int = 3
    dedup: bool = True
    rrf_weights: tuple = (1.0, 1.0)


def dense_dir(chunks, model):
    return config.ARTIFACTS_DIR / f"faiss_{chunks}_{model.replace('/', '__')}"


class Retriever:
    def __init__(self, cfg: RetrieverConfig, chunks=None):
        self.cfg = cfg
        self.chunks = chunks or load_chunks(config.ARTIFACTS_DIR / f"chunks_{cfg.chunks}.jsonl")
        self.bm25 = self.dense = self.reranker = None
        if cfg.mode in ("bm25", "hybrid"):
            self.bm25 = BM25Retriever.load(config.ARTIFACTS_DIR / f"bm25_{cfg.chunks}{cfg.bm25_variant}")
        if cfg.mode in ("dense", "hybrid"):
            from .dense import DenseIndex
            self.dense = DenseIndex.load(dense_dir(cfg.chunks, cfg.dense_model))
        if cfg.rerank:
            from .dense import Reranker
            self.reranker = Reranker(cfg.reranker_model)
        self.doc_index = DocIdIndex(self.chunks) if cfg.doc_id_boost else None

    def _candidates(self, q, n, restrict=None):
        lists = []
        if self.bm25 is not None:
            lists.append(self.bm25.search(q, k=n, restrict=restrict))
        if self.dense is not None:
            res = self.dense.search(q, k=n if restrict is None else max(n * 20, 400))
            if restrict is not None:
                rs = set(restrict)
                res = [x for x in res if x[0] in rs]
            lists.append(res)
        if len(lists) == 1:
            return lists[0]
        return rrf(lists, weights=list(self.cfg.rrf_weights), top_n=n)

    def retrieve(self, question, top_k=None):
        top_k = top_k or self.cfg.top_k
        n = self.cfg.candidates
        cand = []
        if self.doc_index is not None:
            _, hits = self.doc_index.chunks_for_question(question)
            if hits:
                cand = self._candidates(question, n, restrict=hits)
        if len(cand) < n:
            seen = {i for i, _ in cand}
            cand += [x for x in self._candidates(question, n) if x[0] not in seen]
        if self.cfg.dedup:
            cand = dedup_by_text(cand, self.chunks, max_per_doc=self.cfg.max_per_doc)
        if self.reranker is not None:
            cand = self.reranker.rerank(question, cand[:n], [chunk_to_index_text(self.chunks[i]) for i, _ in cand[:n]],
                                        top_n=top_k)
        return [dict(self.chunks[i], score=s) for i, s in cand[:top_k]]
