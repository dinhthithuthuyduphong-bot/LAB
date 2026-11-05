"""Step 1 (CPU): clean every corpus file and extract metadata.

Outputs
  artifacts/docs.jsonl     one cleaned document per line (large, git-ignored)
  data/corpus_meta.csv     metadata only (file, doc_id, year, type, issuer, title, length)

Usage:  python -I scripts/build_corpus.py
"""
import sys, os, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from tqdm import tqdm

from src import config
from src.legal_text import clean_text, extract_metadata, split_info_block


def main():
    files = sorted(f for f in os.listdir(config.CORPUS_DIR) if f.endswith(".txt"))
    config.ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    with open(config.ARTIFACTS_DIR / "docs.jsonl", "w", encoding="utf-8") as out:
        for f in tqdm(files, desc="Cleaning corpus"):
            raw = (config.CORPUS_DIR / f).read_text(encoding="utf-8", errors="replace")
            text = clean_text(raw)
            _, info = split_info_block(raw)
            meta = extract_metadata(f, text, info)
            meta["raw_chars"] = len(raw)
            meta["chars"] = len(text)
            meta["n_dieu"] = text.count("\nĐiều ")
            rows.append(meta)
            out.write(json.dumps({**meta, "text": text}, ensure_ascii=False) + "\n")
    df = pd.DataFrame(rows)
    df.to_csv(config.DATA_DIR / "corpus_meta.csv", index=False)
    print(f"{len(df)} documents -> {config.ARTIFACTS_DIR / 'docs.jsonl'}")
    print(f"total chars: raw={df.raw_chars.sum():,} cleaned={df.chars.sum():,}")


if __name__ == "__main__":
    main()
