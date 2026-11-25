# RAG Law Chatbot: cải tiến so với Baseline

> Đề bài nằm trong `doc/` (`RAG_Assignment.pdf`, `Baseline.ipynb`, `RES.xlsx`).
> Tác giả: Đinh Thị Thu Thủy (MSHV 2570508), môn Mô hình ngôn ngữ lớn, nhóm CH01.
> Báo cáo: [`report/latex/main.pdf`](report/latex/main.pdf) (bản Markdown: [`report/report.md`](report/report.md)).
> Video demo: https://youtu.be/sOus4EisfnE


## Nội dung bài nộp

Toàn bộ bài nộp nằm trong repo này, nhánh `RAG-based-chatbot-system`. Người đọc chỉ cần clone về là chạy lại được, không phải tải thêm gì.

| Thành phần | Ở đâu | Ghi chú |
|---|---|---|
| **Source code** | `src/`, `scripts/`, `app/`, `notebooks/`, `tests/` | Mô tả từng file ở mục [Cấu trúc](#cấu-trúc) |
| **Dataset** | `Dataset/export_1/` (16.439 văn bản .txt, khoảng 442MB), `doc/RES.xlsx` (2.745 cặp QA) | Đã nằm trong git. `data/` chứa tập eval 200 câu cố định (seed 42) sinh từ RES.xlsx |
| **Manual** | File này: [Cài đặt](#cài-đặt), [Kiểm tra nhanh](#kiểm-tra-nhanh-không-cần-gpu-khoảng-10-phút), [Chạy lại từ đầu](#chạy-lại-từ-đầu), [Demo](#demo) | Phụ lục A của báo cáo PDF tóm tắt lại các bước này |
| Kết quả đã chạy | `results/` (câu trả lời từng câu, metric, EDA, retrieval) | Dùng để đối chiếu khi chạy lại |

Lấy mã nguồn và dữ liệu:

```bash
git clone -b RAG-based-chatbot-system https://github.com/dinhthithuthuyduphong-bot/LAB.git
```

```bash
cd LAB
```

**Môi trường đã kiểm tra:** phần CPU chạy lại từ một bản clone sạch trên Linux, Python 3.13, RAM 16GB, kết quả khớp với số đã nộp (xem mục dưới).
Phần GPU chạy trên Kaggle (GPU T4 miễn phí), bằng `notebooks/run_on_kaggle.ipynb`.

Danh sách việc đã làm và chi phí: [`doc/TODO.md`](doc/TODO.md).

## Kết quả (200 câu, Kaggle T4)

| Cấu hình | Cosine | Jaccard | Token Overlap | BLEU | ROUGE-L |
|---|---|---|---|---|---|
| Baseline (gốc) | 0,6991 | 0,2012 | 0,7675 (*) | 0,1173 | 0,0959 |
| **Hệ thống cải tiến (E)** | **0,7636** | **0,3063** | 0,3692 | **0,2740** | **0,2463** |

(*) Output của baseline gốc có lẫn toàn bộ prompt và ngữ cảnh (khoảng 2.400 từ), nên Token Overlap cao giả tạo.
So với baseline chỉ tính phần sinh ra, hệ thống cải tiến tốt hơn ở cả 5 chỉ số. Chi tiết: [`report/report.md`](report/report.md).

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
app/notebook_ui.py       ô hỏi–đáp ngay trong notebook (Kaggle/Colab), không cần link ngoài
notebooks/               run_on_kaggle.ipynb (toàn bộ pipeline GPU), demo.ipynb,
                         demo_chatbox.ipynb (bản demo đã chạy trên Kaggle T4, có output, dùng để quay video)
report/latex/            báo cáo LaTeX (main.tex + figures/), import vào Overleaf: report/overleaf_report.zip
results/                 eda/, retrieval/, predictions/, metrics/
tests/test_core.py       kiểm tra nhanh các phần CPU
tests/smoke_gpu_path.py  chạy thử toàn bộ nhánh GPU bằng model tí hon tạo trên máy (không tải gì, CPU chạy được)
artifacts/               (git-ignored) chunk, chỉ mục BM25/FAISS, build lại bằng scripts
requirements.txt         thư viện cho phần CPU; requirements-gpu.txt thêm phần GPU
requirements-lock.txt    phiên bản CPU chính xác đã kiểm tra chạy lại từ bản clone sạch
```

🟢 = chạy trên CPU · 🟡 = cần GPU (Kaggle hoặc Colab miễn phí là đủ).

## Cài đặt

Cần Python 3.10 trở lên.

```bash
pip install -r requirements.txt
```

Nếu bản mới nhất của một thư viện nào đó bị lỗi, cài đúng các phiên bản đã kiểm tra:

```bash
pip install -r requirements-lock.txt
```

Nếu chạy trên máy có GPU (Kaggle/Colab), cài thêm:

```bash
pip install -r requirements-gpu.txt
```

Các script đều chạy được bằng `python -I scripts/<tên>.py` từ bất kỳ thư mục nào. Cờ `-I` dùng để cô lập môi trường, không bắt buộc.

## Kiểm tra nhanh (không cần GPU, khoảng 10 phút)

Các bước dưới đây chạy hết trên CPU. Chúng kiểm tra lại được: số liệu khám phá dữ liệu, kết quả retrieval, 4 metric từ vựng của mọi cấu hình, và demo.

**1. Tính lại metric từ câu trả lời đã lưu** (vài giây). Câu trả lời của 200 câu cho mọi cấu hình nằm trong `results/predictions/`.

```bash
python -I scripts/evaluate.py --no-cosine
```

Lệnh này tính lại Jaccard, Token Overlap, BLEU và ROUGE-L. Cosine cần model embedding nên được giữ nguyên từ lần chạy GPU (bỏ `--no-cosine` để tính lại, khoảng 5 phút trên CPU).
Kết quả phải trùng với bảng sau. Có thể kiểm tra bằng lệnh dưới đây: nếu lệnh không in ra gì thì kết quả đã khớp.

```bash
git diff results/metrics/summary.csv
```

Các file kết quả từng câu (`results/metrics/<cấu hình>.csv`) có thể khác ở chữ số thập phân thứ 16, tùy phiên bản pandas. Khác biệt này không ảnh hưởng đến kết quả. Muốn đưa các file về như cũ thì chạy `git checkout results/metrics`.

| Cấu hình (200 câu) | Cosine | Jaccard | Token Overlap | BLEU | ROUGE-L |
|---|---|---|---|---|---|
| baseline | 0,6991 | 0,2012 | 0,7675 | 0,1173 | 0,0959 |
| baseline_noecho | 0,5768 | 0,1510 | 0,1064 | 0,0426 | 0,1127 |
| E_full_fewshot (hệ thống cuối) | 0,7636 | 0,3063 | 0,3692 | 0,2740 | 0,2463 |

**2. Dựng lại dữ liệu, chunk và chỉ mục BM25** (khoảng 5 phút). Đây là các lệnh ở mục [Bước CPU](#-bước-cpu-khoảng-5-phút-ram--8gb) bên dưới.
Kết quả đúng khi:
- `build_corpus.py` in ra `16439 documents`;
- `prepare_data.py` in ra `eval_set.csv: 200 rows ({'not_covered': 149, 'covered': 51})`;
- `build_chunks.py --strategy legal` in ra `384,612 chunks`;
- `eval_retrieval.py` in ra `hybrid_legal_rerank` có DocRecall@1 = 0,608 và DocRecall@5 = 0,863 (đọc lại từ file kết quả có sẵn), còn `bm25_legal` có DocRecall@5 = 0,784.

`data/` và `results/eda/` sinh ra giống hệt bản đã nộp.

**3. Chạy demo không cần GPU.** Demo chỉ hiện các đoạn văn bản tìm được, chưa có LLM sinh câu trả lời. Cần làm bước 2 trước.

```bash
python -I app/demo.py --llm extractive --cli "Mức lương cơ sở từ 01/7/2024 là bao nhiêu?"
```

Kết quả đúng: nguồn đầu tiên là Kết luận 83-KL/TW, có đoạn "điều chỉnh mức lương cơ sở từ 1,8 triệu đồng lên 2,34 triệu đồng … kể từ ngày 01/7/2024".

Bản demo đầy đủ có LLM chạy trên GPU (xem mục [Demo](#demo)). Nếu không có GPU, xem `notebooks/demo_chatbox.ipynb`: notebook này đã có sẵn output của lần chạy trên Kaggle.

## Chạy lại từ đầu

### 🟢 Bước CPU (khoảng 5 phút, RAM ≥ 8GB)

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

Video demo: https://youtu.be/sOus4EisfnE

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
  Em báo cáo cả `baseline` (giữ nguyên hành vi này, coi là số chính thức) và `baseline_noecho` (chỉ phần sinh ra).
- **Cosine** luôn được tính bằng `keepitreal/vietnamese-sbert`, cùng embedding với baseline, để so sánh công bằng.
- **Corpus và câu hỏi lệch nhau:** 100% văn bản thuộc lĩnh vực *Lao động – Tiền lương*, trong khi phần lớn câu hỏi về ngân hàng.
  Chỉ 8/314 văn bản được hỏi có trong corpus. Chi tiết xem `results/eda/eda_summary.md`.
