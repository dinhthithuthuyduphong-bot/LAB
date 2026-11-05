"""Generate notebooks/run_on_kaggle.ipynb and notebooks/demo.ipynb (keeps notebooks in sync with the scripts).

Usage: python -I scripts/make_notebooks.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def nb(cells):
    out = []
    for kind, src in cells:
        c = {"cell_type": kind, "metadata": {}, "source": src.strip("\n").splitlines(keepends=True)}
        if kind == "code":
            c.update(outputs=[], execution_count=None)
        out.append(c)
    return {"cells": out, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                       "language_info": {"name": "python"}, "accelerator": "GPU"},
            "nbformat": 4, "nbformat_minor": 5}


SETUP = r'''
# Settings -> Accelerator: GPU (T4 x2 or P100), Internet: ON
import os, subprocess
REPO = "https://github.com/dinhthithuthuyduphong-bot/LAB.git"
BRANCH = "RAG-based-chatbot-system"
WORK = "/kaggle/working/LAB" if os.path.exists("/kaggle") else "/content/LAB"
if not os.path.exists(WORK):
    subprocess.run(["git", "clone", "--depth", "1", "-b", BRANCH, REPO, WORK], check=True)
os.chdir(WORK)
# Large artifacts (chunks / BM25 / FAISS) can be kept in a Kaggle Dataset or Google Drive between sessions:
# os.environ["ARTIFACTS_DIR"] = "/kaggle/input/lab-rag-artifacts"   # read-only input -> copy if you need to write
!pip install -q -r requirements-gpu.txt
!nvidia-smi --query-gpu=name,memory.total --format=csv
'''

KAGGLE = [
    ("markdown", """
# RAG Law Chatbot — chạy toàn bộ trên GPU miễn phí (Kaggle / Colab)

Thứ tự chạy (ước lượng thời gian trên T4):

| Bước | Việc | Thời gian |
|---|---|---|
| 1 | Clone repo + cài thư viện | khoảng 3 phút |
| 2 | Làm sạch corpus, chunk, BM25 (CPU) | khoảng 6 phút, **bỏ qua** nếu đã có `artifacts/` |
| 3 | FAISS index baseline (sbert, chunk 2000) | khoảng 20–40 phút |
| 4 | Chạy baseline, N = 200 câu | khoảng 30–60 phút |
| 5 | FAISS index cho pipeline mới | khoảng 30–60 phút |
| 6 | Chạy các cấu hình cải tiến (mỗi cấu hình) | khoảng 1–2 giờ |
| 7 | Tính metric (có cosine) | khoảng 2 phút |

Mọi kết quả được cache trong `results/predictions/*.csv`. Nếu phiên bị ngắt, chỉ cần chạy lại cell đó, các câu đã xong sẽ được bỏ qua.
"""),
    ("code", SETUP),
    ("markdown", "## 2. Dữ liệu + chunk + BM25 (CPU, chạy 1 lần)"),
    ("code", """
!python -I scripts/build_corpus.py
!python -I scripts/prepare_data.py --n 200
!python -I scripts/build_chunks.py --strategy baseline
!python -I scripts/build_chunks.py --strategy legal
!python -I scripts/build_bm25.py --chunks legal
"""),
    ("markdown", "## 3–4. Baseline (đúng như `doc/Baseline.ipynb`, nhưng chạy trên cùng 200 câu với các cấu hình khác)"),
    ("code", """
!python -I scripts/build_dense.py --chunks baseline --model keepitreal/vietnamese-sbert
# faithful: the prompt is echoed in the output (LangChain HuggingFacePipeline default) -> official baseline numbers
!python -I scripts/run_rag.py --name baseline --retriever baseline --llm baseline --fewshot none --batch-size 1
# fixed: only the generated text is evaluated
!python -I scripts/run_rag.py --name baseline_noecho --retriever baseline --llm baseline-noecho --fewshot none --batch-size 1
"""),
    ("markdown", "## 5. Index cho pipeline cải tiến"),
    ("code", """
# (optional) quick embedding comparison on a subset before embedding everything
# !python -I scripts/build_dense.py --chunks legal --model intfloat/multilingual-e5-base --subset 20000
!python -I scripts/build_dense.py --chunks legal --model bkai-foundation-models/vietnamese-bi-encoder
!python -I scripts/eval_retrieval.py --configs bm25_legal dense_legal hybrid_legal hybrid_legal_rerank --k 5
"""),
    ("markdown", """
## 6. Ablation: mỗi dòng thay một thành phần
Debug trước với `--limit 5`, sau đó bỏ `--limit` để chạy đủ 200 câu.
"""),
    ("code", """
LLM = "Qwen/Qwen2.5-3B-Instruct"
runs = [
    # name                    retriever               extra args
    ("A_llm_prompt",          "baseline",             "--fewshot none"),      # only LLM + prompt changed
    ("B_bm25_legal",          "bm25_legal",           "--fewshot none"),      # + structure-aware chunks, BM25
    ("C_hybrid",              "hybrid_legal",         "--fewshot none"),      # + dense (hybrid RRF)
    ("D_hybrid_rerank",       "hybrid_legal_rerank",  "--fewshot none"),      # + cross-encoder rerank
    ("E_full_fewshot",        "hybrid_legal_rerank",  "--fewshot static"),    # + 1 few-shot example (style)
]
for name, retr, extra in runs:
    !python -I scripts/run_rag.py --name {name} --retriever {retr} --llm {LLM} {extra} --batch-size 4
"""),
    ("code", """
# Optional ablation, report it separately: similar QA pairs from the pool (never the eval questions) as extra reference
!python -I scripts/run_rag.py --name F_full_qamemory --retriever hybrid_legal_rerank --llm Qwen/Qwen2.5-3B-Instruct --fewshot static --qa-memory 2
"""),
    ("markdown", "## 7. Metric (5 chỉ số, cosine dùng cùng embedding với baseline)"),
    ("code", """
!python -I scripts/evaluate.py
import pandas as pd
s = pd.read_csv("results/metrics/summary.csv")
s[s.group == "all"].sort_values("ROUGE_L")
"""),
    ("code", """
# Save results back (download, or commit from the notebook if you have a token configured)
!zip -qr results.zip results && ls -la results.zip
"""),
]

DEMO = [
    ("markdown", """
# Demo – Chatbot pháp luật (RAG)
Cần GPU để chạy LLM. Nếu không có GPU, đặt `LLM = "extractive"` để xem phần retrieval.
"""),
    ("code", SETUP),
    ("code", """
import os
if not os.path.exists("artifacts/bm25_legal"):
    !python -I scripts/build_corpus.py && python -I scripts/prepare_data.py && python -I scripts/build_chunks.py --strategy legal && python -I scripts/build_bm25.py --chunks legal
"""),
    ("code", """
import sys; sys.path.insert(0, "."); sys.path.insert(0, "app"); sys.path.insert(0, "scripts")
from demo import Bot, EXAMPLES
LLM = "Qwen/Qwen2.5-3B-Instruct"     # or "extractive"
RETRIEVER = "bm25_legal"             # "hybrid_legal_rerank" once the FAISS index is built
bot = Bot(RETRIEVER, LLM)
"""),
    ("code", """
from IPython.display import Markdown, display
for q in EXAMPLES:
    ans, src = bot.answer(q)
    display(Markdown(f"### ❓ {q}\\n\\n{ans}\\n\\n<details><summary>Nguồn</summary>\\n\\n{src}\\n</details>"))
"""),
    ("code", """
# Interactive UI with a public link (Gradio, free)
!python -I app/demo.py --retriever {RETRIEVER} --llm {LLM}
"""),
]


def main():
    (ROOT / "notebooks").mkdir(exist_ok=True)
    for name, cells in [("run_on_kaggle.ipynb", KAGGLE), ("demo.ipynb", DEMO)]:
        (ROOT / "notebooks" / name).write_text(json.dumps(nb(cells), ensure_ascii=False, indent=1), encoding="utf-8")
        print("wrote notebooks/" + name)


if __name__ == "__main__":
    main()
