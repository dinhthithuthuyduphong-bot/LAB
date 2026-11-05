"""Step 4 (CPU): chunk the cleaned corpus.

Usage:
  python -I scripts/build_chunks.py --strategy legal     # -> artifacts/chunks_legal.jsonl
  python -I scripts/build_chunks.py --strategy baseline  # -> artifacts/chunks_baseline.jsonl

Each line: {chunk_id, file, doc_id, doc_id_norm, year, doc_type, status, header, dieu, text}
For the improved pipeline the text to embed/index is `header + "\n" + text`.
"""
import sys, json, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
from tqdm import tqdm

from src import config
from src.chunking import baseline_chunks, legal_chunks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strategy", choices=["legal", "baseline"], default="legal")
    ap.add_argument("--size", type=int, default=None)
    ap.add_argument("--overlap", type=int, default=None)
    a = ap.parse_args()
    size = a.size or (config.CHUNK_SIZE if a.strategy == "legal" else config.BASELINE_CHUNK_SIZE)
    overlap = a.overlap if a.overlap is not None else (
        config.CHUNK_OVERLAP if a.strategy == "legal" else config.BASELINE_CHUNK_OVERLAP)

    out_path = config.ARTIFACTS_DIR / f"chunks_{a.strategy}.jsonl"
    lens, n = [], 0
    with open(config.ARTIFACTS_DIR / "docs.jsonl", encoding="utf-8") as f, open(out_path, "w", encoding="utf-8") as out:
        for line in tqdm(f, total=16439, desc=f"Chunking ({a.strategy}, {size}/{overlap})", mininterval=5):
            d = json.loads(line)
            base = {k: d.get(k) for k in ["file", "doc_id", "doc_id_norm", "year", "doc_type", "status"]}
            if a.strategy == "baseline":
                raw = (config.CORPUS_DIR / d["file"]).read_text(encoding="utf-8", errors="replace")
                items = [{"text": t, "header": "", "dieu": ""} for t in baseline_chunks(raw, size, overlap)]
            else:
                items = legal_chunks(d["text"], d, size, overlap)
            for it in items:
                rec = {"chunk_id": n, **base, "header": it["header"], "dieu": it["dieu"], "text": it["text"]}
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                lens.append(len(it["text"]))
                n += 1
    lens = np.array(lens)
    print(f"{n:,} chunks -> {out_path}")
    print(f"chunk length: mean={lens.mean():.0f} median={np.median(lens):.0f} p95={np.percentile(lens, 95):.0f} max={lens.max()}")


if __name__ == "__main__":
    main()
