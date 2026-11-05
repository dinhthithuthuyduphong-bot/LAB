"""Dense retrieval (FAISS) and cross-encoder reranking.  🟡 Needs a GPU for reasonable speed.

Written to run on Kaggle / Colab (torch + sentence-transformers + faiss). Not executed in the CPU-only
development environment because it needs model downloads from HuggingFace.
"""
import json
from pathlib import Path

import numpy as np

# Models that expect Vietnamese word segmentation (PhoBERT-based)
WORD_SEGMENTED_MODELS = {"bkai-foundation-models/vietnamese-bi-encoder", "VoVanPhuc/sup-SimCSE-VietNamese-phobert-base",
                         "keepitreal/vietnamese-sbert"}
# Models that expect "query: " / "passage: " prefixes
E5_MODELS = ("intfloat/multilingual-e5",)


def _segment(texts):
    from pyvi import ViTokenizer
    return [ViTokenizer.tokenize(t) for t in texts]


class Embedder:
    def __init__(self, model_name, device=None, max_seq_length=256, batch_size=128, fp16=True):
        from sentence_transformers import SentenceTransformer
        import torch
        device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.name = model_name
        self.model = SentenceTransformer(model_name, device=device)
        self.model.max_seq_length = max_seq_length
        if fp16 and device == "cuda":
            self.model.half()
        self.batch_size = batch_size
        # keepitreal/vietnamese-sbert was used WITHOUT segmentation in the baseline; keep it identical
        self.segment = model_name in WORD_SEGMENTED_MODELS and model_name != "keepitreal/vietnamese-sbert"

    def _prep(self, texts, kind):
        if self.segment:
            texts = _segment(texts)
        if self.name.startswith(E5_MODELS):
            texts = [f"{kind}: {t}" for t in texts]
        return texts

    def encode(self, texts, kind="passage", show_progress=False):
        return self.model.encode(self._prep(list(texts), kind), batch_size=self.batch_size, normalize_embeddings=True,
                                 convert_to_numpy=True, show_progress_bar=show_progress).astype(np.float32)

    def __call__(self, texts):  # used by metrics.cosine_scores
        return self.encode(texts, kind="query")


class DenseIndex:
    def __init__(self, embedder: Embedder):
        self.emb = embedder
        self.index = None

    def build(self, texts, batch=8192):
        import faiss
        from tqdm import tqdm
        for i in tqdm(range(0, len(texts), batch), desc=f"Embedding with {self.emb.name}"):
            v = self.emb.encode(texts[i:i + batch], kind="passage")
            if self.index is None:
                self.index = faiss.IndexFlatIP(v.shape[1])   # cosine (vectors are normalised)
            self.index.add(v)
        return self

    def search(self, query, k=20):
        q = self.emb.encode([query], kind="query")
        s, i = self.index.search(q, k)
        return [(int(a), float(b)) for a, b in zip(i[0], s[0]) if a >= 0]

    def vectors(self, ids):
        return np.stack([self.index.reconstruct(int(i)) for i in ids])

    def save(self, path):
        import faiss
        Path(path).mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, str(Path(path, "index.faiss")))
        Path(path, "cfg.json").write_text(json.dumps({"model": self.emb.name}))

    @classmethod
    def load(cls, path, embedder=None):
        import faiss
        cfg = json.loads(Path(path, "cfg.json").read_text())
        d = cls(embedder or Embedder(cfg["model"]))
        d.index = faiss.read_index(str(Path(path, "index.faiss")))
        return d


class Reranker:
    def __init__(self, model_name="BAAI/bge-reranker-v2-m3", device=None, max_length=512, batch_size=32):
        from sentence_transformers import CrossEncoder
        import torch
        device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = CrossEncoder(model_name, device=device, max_length=max_length)
        self.batch_size = batch_size

    def rerank(self, query, cand, texts, top_n=5):
        """cand: [(idx, score)], texts: list aligned with cand."""
        if not cand:
            return []
        s = self.model.predict([(query, t) for t in texts], batch_size=self.batch_size, show_progress_bar=False)
        order = np.argsort(-np.asarray(s))[:top_n]
        return [(cand[i][0], float(s[i])) for i in order]
