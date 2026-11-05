"""CPU: turn results/*.csv into markdown tables for the report -> report/results_tables.md

Includes the improvement of every run over the official baseline (and over baseline_noecho).
Usage:  python -I scripts/make_tables.py
"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from src import config
from src.metrics import METRIC_NAMES

ORDER = ["baseline", "baseline_noecho", "A_llm_prompt", "B_bm25_legal", "C_hybrid", "D_hybrid_rerank",
         "E_full_fewshot", "F_full_qamemory"]


def fmt(df):
    return df.to_markdown(index=False, floatfmt=".4f")


def main():
    md = ["# Bảng kết quả (sinh tự động bởi `scripts/make_tables.py`)\n"]
    ms = config.RESULTS_DIR / "metrics" / "summary.csv"
    if ms.exists():
        s = pd.read_csv(ms)
        s["order"] = s.name.map(lambda x: ORDER.index(x) if x in ORDER else 99)
        s = s.sort_values(["order", "name"]).drop(columns="order")
        allg = s[s.group == "all"].drop(columns="group")
        md += ["## Kết quả chính (tất cả câu trong eval set)\n", fmt(allg), ""]
        for ref in ["baseline", "baseline_noecho"]:
            if ref in set(allg.name):
                b = allg[allg.name == ref][METRIC_NAMES].iloc[0]
                d = allg[["name"] + METRIC_NAMES].copy()
                for m in METRIC_NAMES:
                    d[m] = (d[m] - b[m]).map(lambda x: f"{x:+.4f}")
                md += [f"## Chênh lệch so với `{ref}`\n", d.to_markdown(index=False), ""]
        for grp in ["covered", "not_covered"]:
            g = s[s.group == grp].drop(columns="group")
            if len(g):
                md += [f"## Nhóm `{grp}`\n", fmt(g), ""]
    rs = config.RESULTS_DIR / "retrieval" / "retrieval_summary.csv"
    if rs.exists():
        md += ["## Retrieval (không LLM)\n", fmt(pd.read_csv(rs).sort_values(["k", "config"])), ""]
    rows = []
    for c in sorted((config.RESULTS_DIR / "predictions").glob("*.config.json")):
        cfg = json.loads(c.read_text())
        p = pd.read_csv(c.with_name(c.name.replace(".config.json", ".csv")))
        rows.append({"name": c.name.replace(".config.json", ""), "retriever": cfg.get("retriever"), "llm": cfg.get("llm"),
                     "fewshot": cfg.get("fewshot"), "qa_memory": cfg.get("qa_memory"), "n": len(p),
                     "sec_per_q": round(p.sec_per_q.mean(), 2), "max_gpu_gb": cfg.get("max_gpu_memory_gb")})
    if rows:
        md += ["## Cấu hình và chi phí chạy\n", pd.DataFrame(rows).to_markdown(index=False), ""]
    out = config.REPORT_DIR / "results_tables.md"
    out.write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
