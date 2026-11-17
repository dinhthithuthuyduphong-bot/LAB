"""CPU: figures for the LaTeX report -> report/latex/figures/ (also copies the EDA figures there).

Usage:  python -I scripts/make_report_figures.py
"""
import sys, shutil
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src import config

OUT = config.REPORT_DIR / "latex" / "figures"
plt.rcParams.update({"figure.dpi": 150, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.alpha": 0.3, "font.size": 9, "axes.axisbelow": True})
GREY, BLUE, ORANGE, GREEN = "#9e9e9e", "#2a6fdb", "#e07a2e", "#2e9d5b"
RUNS = [("baseline", "Baseline"), ("baseline_noecho", "Baseline\n(no-echo)"), ("A_llm_prompt", "A\nLLM+prompt"),
        ("B_bm25_legal", "B\n+chunk Điều\n+BM25"), ("C_hybrid", "C\n+hybrid"), ("D_hybrid_rerank", "D\n+rerank"),
        ("E_full_fewshot", "E\n+few-shot")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for f in ["topic_mismatch", "year_mismatch", "qa_lengths", "qa_top_refs", "corpus_doc_types", "corpus_fields",
              "qa_question_types", "corpus_length"]:
        shutil.copy(config.RESULTS_DIR / "eda" / f"{f}.png", OUT / f"{f}.png")

    s = pd.read_csv(config.RESULTS_DIR / "metrics" / "summary.csv")
    allg = s[s.group == "all"].set_index("name")
    names = [n for n, _ in RUNS]
    labels = [l for _, l in RUNS]
    colors = [GREY, GREY] + [BLUE] * 4 + [GREEN]

    # 1) ablation: 4 metrics where both baselines are comparable
    fig, axs = plt.subplots(2, 2, figsize=(9, 5.6))
    short = ["Baseline", "No-echo", "A", "B", "C", "D", "E"]
    for ax, m, t in zip(axs.ravel(), ["ROUGE_L", "BLEU_Score", "Jaccard_Similarity", "Cosine_Similarity"],
                        ["ROUGE-L", "BLEU", "Jaccard", "Cosine"]):
        v = allg.loc[names, m].values
        ax.bar(range(len(v)), v, color=colors)
        ax.set_title(t)
        ax.set_xticks(range(len(v)))
        ax.set_xticklabels(short, fontsize=8)
        for i, x in enumerate(v):
            ax.text(i, x, f"{x:.3f}", ha="center", va="bottom", fontsize=7)
        ax.set_ylim(0, max(v) * 1.18)
    fig.tight_layout()
    fig.savefig(OUT / "ablation_metrics.png")
    plt.close(fig)

    # 2) per group ROUGE-L
    g = s[s.group != "all"].pivot(index="name", columns="group", values="ROUGE_L").loc[names]
    fig, ax = plt.subplots(figsize=(7.5, 3))
    x = np.arange(len(names))
    ax.bar(x - .2, g["covered"], .4, color=ORANGE, label="covered (51 câu)")
    ax.bar(x + .2, g["not_covered"], .4, color=BLUE, label="not_covered (149 câu)")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=7.5)
    ax.set_ylabel("ROUGE-L")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "rouge_by_group.png")
    plt.close(fig)

    # 3) retrieval
    r = pd.read_csv(config.RESULTS_DIR / "retrieval" / "retrieval_summary.csv")
    r = r[r.k == 5].set_index("config")
    order = [("bm25_legal", "BM25"), ("dense_legal", "Dense"), ("hybrid_legal", "Hybrid"), ("hybrid_legal_rerank", "Hybrid\n+rerank")]
    fig, ax = plt.subplots(figsize=(6, 2.8))
    x = np.arange(len(order))
    for i, (m, c) in enumerate([("DocRecall@1(covered)", ORANGE), ("DocRecall@k(covered)", BLUE), ("MRR(covered)", GREEN)]):
        v = r.loc[[o for o, _ in order], m].values
        ax.bar(x + (i - 1) * .27, v, .27, color=c, label=m.replace("(covered)", "").replace("@k", "@5"))
        for xi, vi in zip(x + (i - 1) * .27, v):
            ax.text(xi, vi, f"{vi:.2f}", ha="center", va="bottom", fontsize=6.5)
    ax.set_xticks(x)
    ax.set_xticklabels([l for _, l in order])
    ax.set_ylim(0, 1.15)
    ax.legend(fontsize=7, loc="upper center", ncol=3, frameon=False)
    ax.set_title("Retrieval trên 51 câu covered (chunk theo Điều, k = 5)")
    fig.tight_layout()
    fig.savefig(OUT / "retrieval.png")
    plt.close(fig)
    print("figures ->", OUT)


if __name__ == "__main__":
    main()
