"""🟡 GPU: embed a chunk file and save a FAISS index (build ONCE, then reuse / upload as a Kaggle dataset).

Usage:
  python -I scripts/build_dense.py --chunks baseline --model keepitreal/vietnamese-sbert     # baseline index
  python -I scripts/build_dense.py --chunks legal    --model bkai-foundation-models/vietnamese-bi-encoder
  python -I scripts/build_dense.py --chunks legal    --model intfloat/multilingual-e5-base --subset 2000   # quick model comparison
Output: artifacts/faiss_<chunks>_<model>/
"""
import sys, argparse, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import config
from src.dense import DenseIndex, Embedder
from src.retrieval import load_chunks, chunk_to_index_text
from src.retriever import dense_dir


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunks", default="legal")
    ap.add_argument("--model", default=None, help="default: baseline embedding for --chunks baseline, else EMBEDDING_MODEL")
    ap.add_argument("--max-seq-length", type=int, default=None, help="default: the model's own limit")
    ap.add_argument("--batch-size", type=int, default=128)
    ap.add_argument("--subset", type=int, default=None, help="only the first N chunks (for quick comparisons)")
    a = ap.parse_args()
    a.model = a.model or (config.BASELINE_EMBEDDING if a.chunks == "baseline" else config.EMBEDDING_MODEL)
    t0 = time.time()
    chunks = load_chunks(config.ARTIFACTS_DIR / f"chunks_{a.chunks}.jsonl", fields=("header", "text"))
    # the baseline embeds the (lowercased) chunk text only; our chunks carry a header
    texts = [c["text"] if a.chunks == "baseline" else chunk_to_index_text(c) for c in chunks]
    if a.subset:
        texts = texts[:a.subset]
    baseline = a.chunks == "baseline"
    # baseline = LangChain HuggingFaceEmbeddings (no normalisation) + FAISS.from_texts (IndexFlatL2)
    emb = Embedder(a.model, max_seq_length=a.max_seq_length, batch_size=a.batch_size, normalize=not baseline)
    idx = DenseIndex(emb, metric="l2" if baseline else "ip").build(texts)
    out = dense_dir(a.chunks, a.model) if not a.subset else Path(str(dense_dir(a.chunks, a.model)) + f"_sub{a.subset}")
    idx.save(out)
    print(f"{idx.index.ntotal:,} vectors (dim {idx.index.d}) -> {out}  ({(time.time() - t0) / 60:.1f} min)")


if __name__ == "__main__":
    main()
