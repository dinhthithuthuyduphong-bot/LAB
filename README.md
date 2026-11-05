# RAG Law Chatbot: cải tiến so với Baseline

> Đề bài nằm trong `doc/` (`RAG_Assignment.pdf`, `Baseline.ipynb`, `RES.xlsx`).
> Bài nộp gồm: **source code**, **dataset**, **manual** (file này) để người đọc chạy lại được kết quả.
> Danh sách việc cần làm và chi phí: [`doc/TODO.md`](doc/TODO.md). Bản nháp báo cáo: [`report/report.md`](report/report.md).

## Cấu trúc

```
Dataset/export_1/        16.439 văn bản .txt (corpus)
doc/                     đề bài, baseline notebook, RES.xlsx (QA), TODO
data/                    res.csv, eval_set.csv (200 câu cố định), fewshot_pool.csv, corpus_meta.csv
src/                     thư viện
  config.py              mọi tham số (ghi đè được bằng biến môi trường)
  legal_text.py          làm sạch văn bản, tách metadata "THÔNG TIN THÊM", nhận diện số hiệu
  chunking.py            chunk baseline (2000/50) + chunk theo Chương/Điều (1000/150, có header)
  retrieval.py           BM25 (scipy sparse), tăng hạng theo số hiệu, RRF, MMR, khử trùng lặp
  retriever.py           retriever cấu hình được: bm25 | dense | hybrid (+ rerank)
  dense.py        🟡     embedding + FAISS + cross-encoder reranker
  llm.py          🟡     LLM instruct (chat template) và LLM baseline
  prompts.py             prompt baseline + prompt cải tiến
  fewshot.py             chọn ví dụ few-shot, chỉ lấy từ fewshot_pool
  postprocess.py         làm sạch output
  metrics.py             5 metric, giống hệt công thức của baseline
scripts/                 các bước chạy (xem bên dưới)
app/demo.py              demo CLI / Gradio
notebooks/               run_on_kaggle.ipynb (toàn bộ pipeline GPU), demo.ipynb
results/                 eda/, retrieval/, predictions/, metrics/
tests/test_core.py       kiểm tra nhanh các phần CPU
tests/smoke_gpu_path.py  chạy thử toàn bộ nhánh GPU bằng model tí hon tạo trên máy (không tải gì, CPU chạy được)
artifacts/               (git-ignored) chunk, chỉ mục BM25/FAISS, build lại bằng scripts
```

🟢 = chạy trên CPU · 🟡 = cần GPU (Kaggle hoặc Colab miễn phí là đủ).

## Cài đặt

```bash
pip install -r requirements.txt
```

Nếu chạy trên máy có GPU (Kaggle/Colab), cài thêm:

```bash
pip install -r requirements-gpu.txt
```

Các script đều chạy được bằng `python -I scripts/<tên>.py` từ bất kỳ thư mục nào. Cờ `-I` dùng để cô lập môi trường, không bắt buộc.

## Chạy lại từ đầu

### 🟢 Bước CPU (khoảng 8 phút, RAM ≥ 8GB)

```bash
python -I scripts/build_corpus.py
```

Làm sạch 16.439 file, tách metadata: tạo ra `artifacts/docs.jsonl` và `data/corpus_meta.csv`.

```bash
python -I scripts/prepare_data.py --n 200
```

Chuyển RES.xlsx sang `data/res.csv`, tạo `eval_set.csv` (200 câu, seed 42) và `fewshot_pool.csv`.

```bash
python -I scripts/eda.py
```

Khám phá dữ liệu: ghi kết quả vào `results/eda/eda_summary.md` và các hình.

```bash
python -I scripts/build_chunks.py --strategy legal
```

```bash
python -I scripts/build_chunks.py --strategy baseline
```

```bash
python -I scripts/build_bm25.py --chunks legal
```

```bash
python -I scripts/build_bm25.py --chunks baseline
```

```bash
python -I scripts/eval_retrieval.py --k 5
```

Đánh giá retrieval (BM25), ghi vào `results/retrieval/retrieval_summary.csv`.

```bash
python -I tests/test_core.py
```

### 🟡 Bước GPU

Mở `notebooks/run_on_kaggle.ipynb` trên Kaggle (GPU T4/P100, bật Internet) rồi chạy lần lượt từng cell. Tương đương với các lệnh sau:

```bash
python -I scripts/build_dense.py --chunks baseline --model keepitreal/vietnamese-sbert
```

```bash
python -I scripts/run_rag.py --name baseline --retriever baseline --llm baseline --fewshot none --batch-size 1
```

```bash
python -I scripts/build_dense.py --chunks legal --model bkai-foundation-models/vietnamese-bi-encoder
```

```bash
python -I scripts/run_rag.py --name D_hybrid_rerank --retriever hybrid_legal_rerank --llm Qwen/Qwen2.5-3B-Instruct --fewshot none
```

```bash
python -I scripts/evaluate.py
```

Lệnh này tính 5 metric, ghi vào `results/metrics/summary.csv`.

```bash
python -I scripts/error_analysis.py
```

Phân tích lỗi (ví dụ tốt/xấu, tỷ lệ bịa số hiệu), ghi vào `results/analysis/`. Chạy trên CPU.

```bash
python -I scripts/make_tables.py
```

Sinh bảng kết quả cho báo cáo vào `report/results_tables.md`. Chạy trên CPU.

Trước khi chạy thật trên GPU, nên chạy thử nhánh GPU bằng model tí hon (khoảng 5 phút, không tốn quota vì chạy được trên CPU):

```bash
python -I tests/smoke_gpu_path.py
```

Câu trả lời được cache trong `results/predictions/<name>.csv`. Nếu phiên bị ngắt, chạy lại lệnh đó: các câu đã có sẽ được bỏ qua. Tính lại metric không cần GPU (thêm `--no-cosine` nếu không muốn tải model embedding).

### Kiểm tra nhanh khi không có GPU

Lệnh sau chạy toàn bộ pipeline nhưng không gọi LLM, chỉ lấy đoạn trích:

```bash
python -I scripts/run_rag.py --name extractive_bm25_legal_k5 --retriever bm25_legal --llm extractive --fewshot none --max-context-chars 2000
```

Lệnh sau chỉ in prompt cho 3 câu đầu:

```bash
python -I scripts/run_rag.py --name dryrun --retriever bm25_legal --llm dry-run --limit 3
```

## Demo

Giao diện Gradio, tự in ra link công khai (cần GPU):

```bash
python -I app/demo.py
```

Hỏi một câu từ dòng lệnh:

```bash
python -I app/demo.py --cli "Mức lương cơ sở từ 01/7/2024 là bao nhiêu?"
```

Chế độ chỉ dùng CPU (không có LLM, chỉ hiển thị retrieval):

```bash
python -I app/demo.py --llm extractive --cli "Mức lương cơ sở từ 01/7/2024 là bao nhiêu?"
```

## Ghi chú quan trọng
- **Số cặp QA đánh giá: 200** (`data/eval_set.csv`, seed 42). Tập này gồm cả 51 câu có văn bản nguồn trong corpus
  (`covered`) và 149 câu ngẫu nhiên khác (`not_covered`). Mọi cấu hình, kể cả baseline, đều chạy trên đúng 200 câu này.
- **Baseline có lẫn prompt trong output.** `HuggingFacePipeline` của LangChain mặc định `skip_prompt=False`, còn
  transformers mặc định `return_full_text=True`. Vì vậy output của baseline gồm cả prompt và ngữ cảnh.
  Chúng tôi báo cáo cả `baseline` (giữ nguyên hành vi này, coi là số chính thức) và `baseline_noecho` (chỉ phần sinh ra).
- **Cosine** luôn được tính bằng `keepitreal/vietnamese-sbert`, cùng embedding với baseline, để so sánh công bằng.
- **Corpus và câu hỏi lệch nhau:** 100% văn bản thuộc lĩnh vực *Lao động – Tiền lương*, trong khi phần lớn câu hỏi về ngân hàng.
  Chỉ 8/314 văn bản được hỏi có trong corpus. Chi tiết xem `results/eda/eda_summary.md`.
