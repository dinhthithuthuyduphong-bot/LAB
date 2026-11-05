"""Step 2 (CPU): convert RES.xlsx to CSV and create a FIXED evaluation split.

Needs data/corpus_meta.csv (run scripts/build_corpus.py first).

Outputs
  data/res.csv           all 2,745 QA pairs (+ id, ref_norm, in_corpus)
  data/eval_set.csv      EVAL_N questions used for every experiment (baseline and ours)
  data/fewshot_pool.csv  all remaining questions; the only place few-shot examples may come from

The eval set contains ALL questions whose cited document exists in the corpus ("covered") and
is filled up with a random sample of the others, so results can be reported per group.

Usage:  python -I scripts/prepare_data.py [--n 200]
"""
import sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from src import config
from src.legal_text import normalize_doc_id


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=config.EVAL_N)
    args = ap.parse_args()
    assert args.n >= 100, "The assignment requires at least 100 QA pairs"

    raw = pd.read_excel(config.RES_XLSX, sheet_name=0)
    df = pd.DataFrame({
        "id": range(len(raw)),
        "question": raw["Câu Hỏi"].astype(str).str.strip(),
        "answer": raw["Trả lời"].astype(str).str.strip(),
        "ref_doc": raw["Số hiệu VBPL (Trích xuất)"].astype(str).str.strip(),
        "urax_answer": raw["Câu trả lời của URAx-Law"],
        "ref_correct": raw["Reference có đúng không?"],
        "answer_correct": raw["Trả lời có đúng không? "],
    })
    df["ref_norm"] = df.ref_doc.map(normalize_doc_id)

    meta = pd.read_csv(config.DATA_DIR / "corpus_meta.csv")
    known = set(meta.doc_id_norm) | set(meta.file_doc_id_norm)
    df["in_corpus"] = df.ref_norm.isin(known)

    df.to_csv(config.RES_CSV, index=False)
    print(f"res.csv: {len(df)} rows | cited doc in corpus: {df.in_corpus.sum()} rows, "
          f"{df[df.in_corpus].ref_norm.nunique()}/{df.ref_norm.nunique()} unique docs")

    covered = df[df.in_corpus]
    if len(covered) > args.n:
        covered = covered.sample(args.n, random_state=config.SEED)
    rest = df[~df.id.isin(covered.id)].sample(args.n - len(covered), random_state=config.SEED)
    ev = pd.concat([covered, rest]).sort_values("id")
    ev["group"] = ev.in_corpus.map({True: "covered", False: "not_covered"})
    ev.to_csv(config.EVAL_CSV, index=False)
    df[~df.id.isin(ev.id)].to_csv(config.FEWSHOT_CSV, index=False)
    print(f"eval_set.csv: {len(ev)} rows ({ev.group.value_counts().to_dict()}), seed={config.SEED}")
    print(f"fewshot_pool.csv: {len(df) - len(ev)} rows")


if __name__ == "__main__":
    main()
