"""Compute the 5 assignment metrics for cached predictions (results/predictions/*.csv).

Lexical metrics (Jaccard, Token Overlap, BLEU, ROUGE-L) run on CPU. Cosine similarity needs the baseline
embedding model (keepitreal/vietnamese-sbert) — it runs on CPU too, only slower; use --no-cosine to skip.

Usage:
  python -I scripts/evaluate.py                       # every predictions file
  python -I scripts/evaluate.py --names baseline ours_bm25 --no-cosine
  python -I scripts/evaluate.py --baseline-notebook-csv path/to/rag_baseline_metrics.csv   # import old numbers
Outputs: results/metrics/<name>.csv (per question) and results/metrics/summary.csv (+ per group)
"""
import sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from src import config
from src.metrics import METRIC_NAMES, cosine_scores, lexical_metrics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", nargs="*")
    ap.add_argument("--no-cosine", action="store_true")
    a = ap.parse_args()

    pred_dir = config.RESULTS_DIR / "predictions"
    out_dir = config.RESULTS_DIR / "metrics"
    out_dir.mkdir(parents=True, exist_ok=True)
    names = a.names or sorted(p.stem for p in pred_dir.glob("*.csv"))
    ev = pd.read_csv(config.EVAL_CSV)[["id", "answer", "group"]]

    embed = None
    if not a.no_cosine:
        from src.dense import Embedder
        embed = Embedder(config.METRIC_EMBEDDING)   # same model + default max length as the baseline

    summary = []
    for name in names:
        p = pd.read_csv(pred_dir / f"{name}.csv").drop(columns=["group"], errors="ignore")
        df = ev.merge(p[["id", "prediction"]], on="id", how="inner")
        df["prediction"] = df.prediction.fillna("").astype(str)
        lex = pd.DataFrame([lexical_metrics(pr, gt) for pr, gt in zip(df.prediction, df.answer)])
        df = pd.concat([df.reset_index(drop=True), lex], axis=1)
        df["Cosine_Similarity"] = cosine_scores(df.prediction, df.answer, embed) if embed else float("nan")
        df["pred_words"] = df.prediction.str.split().str.len()
        df.drop(columns=["answer"]).to_csv(out_dir / f"{name}.csv", index=False)
        for grp, g in [("all", df)] + list(df.groupby("group")):
            row = {"name": name, "group": grp, "n": len(g), **g[METRIC_NAMES].mean().round(4).to_dict(),
                   "avg_pred_words": round(g.pred_words.mean(), 1)}
            summary.append(row)
        if len(df) < 100:
            print(f"⚠️  {name}: only {len(df)} questions (assignment requires ≥ 100)")

    s = pd.DataFrame(summary)
    path = out_dir / "summary.csv"
    if path.exists():
        old = pd.read_csv(path)
        old = old[~old.name.isin(s.name)]
        # keep cosine computed earlier if this run skipped it
        s = pd.concat([old, s], ignore_index=True)
    s.to_csv(path, index=False)
    print(s[s.group == "all"].to_string(index=False))
    print("\nper group:\n", s[s.group != "all"].to_string(index=False))


if __name__ == "__main__":
    main()
