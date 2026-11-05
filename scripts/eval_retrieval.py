"""Evaluate retrieval alone (no LLM). CPU for BM25 configs; dense/rerank configs need their index / a GPU.

Metrics on the fixed eval set:
  covered group (cited document exists in corpus):
    DocRecall@k  – a chunk of the cited document is in the top-k
    MRR          – 1 / rank of the first chunk of the cited document (within top-k)
  all questions:
    CtxTokenRecall – share of reference-answer tokens that appear in the retrieved context (upper bound
                     of how much the LLM could copy; correlates with Token_Overlap / ROUGE-L)

Usage:
  python -I scripts/eval_retrieval.py --configs bm25_legal bm25_legal_noboost bm25_baseline
"""
import sys, argparse, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
from tqdm import tqdm

from src import config
from src.legal_text import normalize_doc_id
from src.metrics import normalize_text
from src.retriever import Retriever, RetrieverConfig

CONFIGS = {
    # exact baseline retrieval: sbert + FAISS over lowercased 2000/50 chunks, plain top-5
    "baseline":             RetrieverConfig(chunks="baseline", mode="dense", dense_model=config.BASELINE_EMBEDDING,
                                            doc_id_boost=False, dedup=False, candidates=5),
    "bm25_baseline":        RetrieverConfig(chunks="baseline", mode="bm25", doc_id_boost=False, max_per_doc=99),
    "bm25_legal_noboost":   RetrieverConfig(chunks="legal", mode="bm25", doc_id_boost=False),
    "bm25_legal":           RetrieverConfig(chunks="legal", mode="bm25", doc_id_boost=True),
    "dense_legal":          RetrieverConfig(chunks="legal", mode="dense", doc_id_boost=True),
    "hybrid_legal":         RetrieverConfig(chunks="legal", mode="hybrid", doc_id_boost=True),
    "hybrid_legal_rerank":  RetrieverConfig(chunks="legal", mode="hybrid", doc_id_boost=True, rerank=True),
}


def ctx_token_recall(ctx, ans):
    a = set(normalize_text(ans).split())
    c = set(normalize_text(ctx).split())
    return len(a & c) / len(a) if a else 0.0


def run(name, ev, k):
    cfg = CONFIGS[name]
    r = Retriever(cfg)
    rows = []
    for _, q in tqdm(ev.iterrows(), total=len(ev), desc=name, mininterval=5):
        hits = r.retrieve(q.question, top_k=k)
        ref = normalize_doc_id(q.ref_doc)
        rank = next((i + 1 for i, h in enumerate(hits)
                     if h["doc_id_norm"] == ref or normalize_doc_id(h["file"].rsplit(".", 1)[0].replace("_", "/")) == ref), None)
        ctx = "\n".join(h["text"] for h in hits)
        rows.append({"id": q.id, "group": q.group, "rank": rank, "ctx_chars": len(ctx),
                     "CtxTokenRecall": ctx_token_recall(ctx, q.answer),
                     "top_docs": "|".join(h["doc_id"] for h in hits)})
    df = pd.DataFrame(rows)
    cov = df[df.group == "covered"]
    summary = {"config": name, "k": k,
               "DocRecall@1(covered)": float((cov["rank"] == 1).mean()),
               "DocRecall@k(covered)": float(cov["rank"].notna().mean()),
               "MRR(covered)": float(cov["rank"].fillna(np.inf).map(lambda x: 0 if x == np.inf else 1 / x).mean()),
               "CtxTokenRecall(all)": float(df.CtxTokenRecall.mean()),
               "CtxTokenRecall(covered)": float(cov.CtxTokenRecall.mean()),
               "CtxTokenRecall(not_covered)": float(df[df.group == "not_covered"].CtxTokenRecall.mean()),
               "avg_ctx_chars": float(df.ctx_chars.mean())}
    return df, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--configs", nargs="+", default=["bm25_baseline", "bm25_legal_noboost", "bm25_legal"])
    ap.add_argument("--k", type=int, default=5)
    a = ap.parse_args()
    ev = pd.read_csv(config.EVAL_CSV)
    out = config.RESULTS_DIR / "retrieval"
    out.mkdir(parents=True, exist_ok=True)
    sums = []
    for name in a.configs:
        df, s = run(name, ev, a.k)
        df.to_csv(out / f"{name}_k{a.k}.csv", index=False)
        sums.append(s)
        print(json.dumps(s, indent=1))
    path = out / "retrieval_summary.csv"
    allsum = pd.DataFrame(sums)
    if path.exists():
        old = pd.read_csv(path)
        old = old[~((old.config.isin(allsum.config)) & (old.k == a.k))]
        allsum = pd.concat([old, allsum], ignore_index=True)
    allsum.to_csv(path, index=False)
    print(allsum.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
