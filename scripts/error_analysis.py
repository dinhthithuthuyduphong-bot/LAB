"""CPU: error analysis on cached predictions + metrics (for report section 5.4).

For each run: best / worst questions per group, answer-length statistics, how often the model cites a
document number that is NOT in its retrieved context (possible hallucination), and how often it says
"không tìm thấy" (abstains).

Usage:  python -I scripts/error_analysis.py --names baseline E_full_fewshot [--n 3]
Output: results/analysis/<name>.md
"""
import sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from src import config
from src.legal_text import find_doc_ids, normalize_doc_id


def context_texts(retrieved_col, chunks_name):
    """chunk_id -> text for every chunk referenced in the predictions (streams the chunk file once)."""
    import json
    need = {int(x.rsplit("#", 1)[1]) for r in retrieved_col.astype(str) for x in r.split("|") if "#" in x}
    path = config.ARTIFACTS_DIR / f"chunks_{chunks_name}.jsonl"
    out = {}
    if not path.exists():
        return out
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i in need:
                out[i] = json.loads(line)["text"]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", nargs="*")
    ap.add_argument("--n", type=int, default=3)
    a = ap.parse_args()
    mdir, pdir = config.RESULTS_DIR / "metrics", config.RESULTS_DIR / "predictions"
    out = config.RESULTS_DIR / "analysis"
    out.mkdir(parents=True, exist_ok=True)
    ev = pd.read_csv(config.EVAL_CSV)[["id", "question", "answer", "ref_doc"]]
    names = a.names or sorted(p.stem for p in mdir.glob("*.csv") if p.stem != "summary")
    for name in names:
        m = pd.read_csv(mdir / f"{name}.csv")
        p = pd.read_csv(pdir / f"{name}.csv")[["id", "prediction", "retrieved"]]
        df = m.merge(p, on="id", suffixes=("", "_p")).merge(ev, on="id")
        df["prediction"] = df["prediction"].fillna("").astype(str)

        cfg_path = pdir / f"{name}.config.json"
        chunks_name = "legal"
        if cfg_path.exists():
            import json
            retr = json.loads(cfg_path.read_text()).get("retriever", "")
            chunks_name = "baseline" if retr in ("baseline", "bm25_baseline") else "legal"
        texts = context_texts(df.retrieved, chunks_name)

        def cited_not_retrieved(r):
            parts = [x for x in str(r.retrieved).split("|") if "#" in x]
            allowed = {normalize_doc_id(x.rsplit("#", 1)[0]) for x in parts}
            for x in parts:   # numbers written inside the retrieved text may also be cited legitimately
                allowed |= set(find_doc_ids(texts.get(int(x.rsplit("#", 1)[1]), "")))
            cited = set(find_doc_ids(r.prediction))
            return len(cited - allowed) > 0

        df["cites_unretrieved_doc"] = df.apply(cited_not_retrieved, axis=1)
        df["abstains"] = df.prediction.str.lower().str.contains("không tìm thấy|không có thông tin|không đủ thông tin")
        df["starts_can_cu"] = df.prediction.str.strip().str.lower().str.startswith("căn cứ")
        md = [f"# Phân tích lỗi: `{name}`\n", f"Số câu: {len(df)}\n"]
        stats = df.groupby("group").agg(n=("id", "size"), ROUGE_L=("ROUGE_L", "mean"), pred_words=("pred_words", "mean"),
                                        cites_unretrieved=("cites_unretrieved_doc", "mean"), abstains=("abstains", "mean"),
                                        starts_can_cu=("starts_can_cu", "mean")).round(3)
        md += ["## Thống kê theo nhóm\n", stats.to_markdown(), "\n",
               "- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).",
               "- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.\n"]
        for grp, g in df.groupby("group"):
            for title, sub in [("Tốt nhất", g.nlargest(a.n, "ROUGE_L")), ("Kém nhất", g.nsmallest(a.n, "ROUGE_L"))]:
                md.append(f"## {title} – nhóm `{grp}`\n")
                for _, r in sub.iterrows():
                    md.append(f"**Q{r.id}** (ROUGE-L {r.ROUGE_L:.3f}, văn bản tham chiếu `{r.ref_doc}`): {r.question}\n")
                    md.append(f"- *Tham chiếu:* {r.answer[:400]}…\n- *Dự đoán:* {r.prediction[:400]}…\n"
                              f"- *Ngữ cảnh lấy về:* `{str(r.retrieved)[:200]}`\n")
        (out / f"{name}.md").write_text("\n".join(md), encoding="utf-8")
        print(f"wrote {out / (name + '.md')}")
        print(stats.to_string())


if __name__ == "__main__":
    main()
