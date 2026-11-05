"""Step 5 (CPU): build a BM25 index over a chunk file.

Usage:
  python -I scripts/build_bm25.py --chunks legal                  # syllables + bigrams (default)
  python -I scripts/build_bm25.py --chunks legal --no-bigrams
  python -I scripts/build_bm25.py --chunks legal --word-segment   # pyvi, much slower
Output: artifacts/bm25_<chunks>[_variant]/
"""
import sys, argparse, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import config
from src.retrieval import BM25Retriever, load_chunks, chunk_to_index_text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunks", default="legal")
    ap.add_argument("--no-bigrams", action="store_true")
    ap.add_argument("--word-segment", action="store_true")
    a = ap.parse_args()
    variant = ("_uni" if a.no_bigrams else "") + ("_ws" if a.word_segment else "")
    t0 = time.time()
    chunks = load_chunks(config.ARTIFACTS_DIR / f"chunks_{a.chunks}.jsonl", fields=("header", "text"))
    texts = [chunk_to_index_text(c) for c in chunks]
    del chunks
    r = BM25Retriever(bigrams=not a.no_bigrams, word_segment=a.word_segment).fit(texts)
    out = config.ARTIFACTS_DIR / f"bm25_{a.chunks}{variant}"
    r.save(out)
    print(f"BM25 index over {len(texts):,} chunks -> {out}  ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()
