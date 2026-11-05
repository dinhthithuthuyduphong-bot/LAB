# TODO – RAG Law Chatbot (cải tiến so với Baseline)

> **Trạng thái (cập nhật):** đã xong hết các phần 🟢 làm được trên CPU (`[x]`).
> `[~]` = làm một phần. **Nhánh GPU đã được chạy thử toàn bộ** (`tests/smoke_gpu_path.py`, model tí hon tạo trên máy):
> mọi script chạy từ đầu đến cuối không lỗi. Chỉ còn phải chạy với model thật trên Kaggle. Còn lại: các bước 🟡 chạy GPU bằng `notebooks/run_on_kaggle.ipynb`, và vài quyết định của bạn
> (chọn Kaggle hay Colab, có gỡ `Dataset/` khỏi git không, upload Kaggle Dataset).

Nguồn: `doc/RAG_Assignment.pdf`, `doc/Baseline.ipynb`, `doc/RES.xlsx`, `Dataset/export_1/`.

## 💰 Chi phí: phần nào free, phần nào tốn tiền

**Tóm tắt:** toàn bộ bài này có thể làm **0 đồng**.
Mọi model cần dùng (embedding, reranker, LLM dưới 4B) đều là mã nguồn mở, tải miễn phí từ HuggingFace.
Thứ duy nhất tốn kém là **thời gian GPU**, và các GPU miễn phí (Kaggle, Colab Free) là đủ nếu chia việc hợp lý.

| Ký hiệu | Nghĩa | Chạy ở đâu |
|---|---|---|
| 🟢 **FREE – CPU** | Không cần GPU, laptop nào cũng chạy được | Máy cá nhân, Colab/Kaggle CPU |
| 🟡 **FREE – cần GPU** | Miễn phí nhưng phải dùng GPU, bị giới hạn quota | **Kaggle**: 30 giờ GPU/tuần (T4×2 hoặc P100), phiên tối đa 12 giờ, lưu được output/dataset. **Colab Free**: T4, khoảng vài giờ/ngày, hay bị ngắt, không đảm bảo có GPU |
| 🔴 **TỐN TIỀN** | Chỉ là tùy chọn, **không bắt buộc** | Xem bảng dưới |

**Các khoản có thể tốn tiền (đều không bắt buộc):**

| Khoản | Giá tham khảo | Khi nào cần |
|---|---|---|
| Colab Pro | khoảng 10 USD/tháng (100 compute units) | Khi hết quota free hoặc muốn GPU L4/A100 chạy nhanh hơn |
| Colab Pay-as-you-go | khoảng 10 USD cho 100 units (T4 tốn khoảng 1.8 units/giờ) | Chỉ cần thêm vài giờ GPU |
| Thuê GPU (RunPod, Vast.ai…) | khoảng 0.2–0.5 USD/giờ cho T4 hoặc RTX 3090/4090 | Muốn chạy nhiều ablation trong một ngày |
| API LLM trả phí (Gemini, OpenAI…) | tính theo token | **Không nên dùng.** Đề bài yêu cầu LLM dưới 4B. Baseline có import `langchain-google-genai` nhưng không cần dùng |
| Git LFS / lưu trữ | GitHub LFS free 1GB, vượt thì tính phí | Không cần. Dataset đã nằm trong git thường (442MB, file nào cũng dưới 100MB) |

> Giá chỉ để tham khảo, cần kiểm tra lại trên trang của nhà cung cấp lúc mua.

**Ước lượng khối lượng tính toán (để biết quota free có đủ không):**
- Corpus khoảng 430MB text. Với chunk 2000 ký tự thì được khoảng 170k chunk; với chunk khoảng 800 ký tự thì được khoảng 450–550k chunk.
- **Build index (embedding):** dùng model cỡ base (khoảng 135M tham số, như sbert, bi-encoder, e5-base) trên T4 mất khoảng 20–60 phút.
  Dùng `bge-m3` (568M tham số) thì mất khoảng 2–4 giờ. Trên CPU sẽ mất **hàng chục giờ**, nên không nên làm trên CPU.
  → Mỗi cấu hình chỉ build **một lần** rồi lưu index lại để dùng tiếp (Kaggle Dataset hoặc Google Drive).
- **Sinh câu trả lời:** 100–200 câu × khoảng 500 token với Qwen2.5-3B fp16 trên T4 mất khoảng 1–2 giờ cho mỗi cấu hình.
  Ablation khoảng 6 cấu hình thì mất khoảng 6–12 giờ.
- **Tổng cộng:** khoảng 15–25 giờ GPU, vừa đủ trong quota Kaggle free của 1 tuần (30 giờ). Nếu chia ra 2 tuần thì dư dả.

**Mẹo để giữ chi phí 0 đồng:**
1. Làm hết phần 🟢 (code, EDA, BM25, metric) trên máy cá nhân hoặc CPU trước. Chỉ mở GPU khi code đã chạy ổn trên 5–10 câu.
2. Build index một lần rồi lưu lại. Không embed lại corpus mỗi lần mở notebook.
3. Cache câu trả lời của LLM ra file CSV. Khi đổi metric thì không phải sinh lại.
4. Debug với N=10. Chỉ chạy N≥100 cho các lần đo chính thức.
5. Dùng 4-bit (bitsandbytes) nếu bị thiếu VRAM. Model 3B ở 4-bit chỉ cần khoảng 3GB.

---

## Những gì đã biết sau khi đọc repo

**Đề bài:** xây chatbot hỏi đáp luật bằng RAG và cải thiện ít nhất một chỉ số so với baseline:
Cosine, Jaccard, Token Overlap, BLEU (unigram) hoặc ROUGE-L. LLM phải có **dưới 4B tham số**,
và phải đánh giá trên **ít nhất 100 cặp QA**, ghi rõ số cặp đã dùng.

**Thang điểm:** cải thiện so với baseline 3đ · demo 2đ · báo cáo 5đ (khám phá dữ liệu 1đ, phương pháp và kết quả 3đ, trình bày 1đ).
README gốc yêu cầu nộp: **source code, dataset, manual** để người khác chạy lại được.

**Baseline:** chunk 2000 ký tự, overlap 50 → `keepitreal/vietnamese-sbert` → FAISS → top-k=5 →
`Qwen/Qwen1.5-1.8B` (bản *base*, không phải chat), `max_new_tokens=256`, chỉ chạy `df.head(30)`.

**Dữ liệu:**
- Corpus: 16.439 file `.txt`, tên file theo số hiệu (vd `01_2005_QĐ-UB.txt`, có hậu tố `_1`, `_2` khi trùng tên).
  Nhiều nhất là văn bản UBND (~4.700) và HĐND (~1.000), sau đó là LĐTBXH, TTg, CP. Văn bản từ 1957 đến 2025.
  Trong file có ngắt dòng lạ (ví dụ `"VIỆT\n NAM"`).
- RES.xlsx, sheet 1: 2.745 cặp QA. Cột `Câu Hỏi` (trung bình 141 ký tự), `Trả lời` (**trung bình 1.619 ký tự, dài nhất 9.858**),
  `Số hiệu VBPL (Trích xuất)` và `Câu trả lời của URAx-Law`. Chỉ khoảng 132 dòng có nhãn đúng/sai.
  Câu trả lời mẫu thường theo dạng *"Căn cứ tại điểm … khoản … Điều … Thông tư …/…/TT-NHNN quy định …"*.
- RES.xlsx, sheet 2: tần suất trích dẫn của 311 văn bản. Nhiều nhất là 52/2024/NĐ-CP (146 lần), 17/2024/TT-NHNN (86 lần), 39/2016/TT-NHNN (54 lần).

**⚠️ Rủi ro lớn:** trong 315 số hiệu văn bản mà QA trích dẫn, **chỉ có 8 văn bản có trong corpus**.
Các văn bản này chỉ phủ 51/2.745 câu hỏi. Ví dụ, không file nào chứa "50/2024/TT-NHNN" hay "52/2024/NĐ-CP".
Phần lớn câu hỏi về ngân hàng (NHNN) nên khó retrieve đúng ngữ cảnh.
Vì vậy phần cải thiện chỉ số sẽ đến nhiều từ **generation** (prompt, dạng và độ dài câu trả lời) chứ không chỉ từ retrieval.
Cần ghi rõ điểm này trong báo cáo.

---

## 0. Môi trường và cấu trúc dự án — 🟢 FREE
- [ ] 🟢 Chọn nơi chạy GPU. **Đề xuất Kaggle**: free 30 giờ/tuần, ổn định hơn Colab Free. Colab Free dùng làm dự phòng.
- [x] 🟢 Tạo cấu trúc: `src/` (code), `notebooks/`, `results/`, `report/`, `requirements.txt`.
- [x] 🟢 Chuyển `RES.xlsx` sheet 1 thành `res.csv` để không phụ thuộc Google Sheet như baseline.
- [x] 🟢 Gom các tham số (đường dẫn, model, chunk size, k, số câu hỏi N) vào một file config.
- [x] 🟢 Đặt `seed` và generation deterministic (`do_sample=False`) để kết quả lặp lại được.
- [ ] 🟢 Upload `Dataset/export_1` và `res.csv` lên Kaggle Dataset (free, tối đa khoảng 100GB) để notebook GPU đọc trực tiếp.
- [ ] 🟢 Cân nhắc gỡ `Dataset/` khỏi git (442MB) và chỉ hướng dẫn cách tải/giải nén trong manual.

## 1. Khám phá dữ liệu (báo cáo, 1đ) — 🟢 FREE (CPU)
- [x] 🟢 Thống kê corpus: số file, phân bố độ dài, loại văn bản (QĐ, TT, NĐ, NQ, CT…), cơ quan ban hành, năm.
- [x] 🟢 Thống kê QA: độ dài câu hỏi và câu trả lời, phân bố chủ đề và văn bản được trích dẫn (dùng sheet 2), các mẫu câu hỏi.
- [x] 🟢 Đo **độ phủ**: bao nhiêu câu hỏi có văn bản nguồn nằm trong corpus (hiện tại là 51/2.745). Kiểm tra lại bằng cả tên file lẫn nội dung. → 8/314 văn bản, 51/2.745 câu. **100% corpus thuộc lĩnh vực Lao động – Tiền lương.**
- [x] 🟢 Phân tích cấu trúc văn bản (Chương / Mục / Điều / Khoản / Điểm) để thiết kế cách chunk.
- [x] 🟢 Vẽ biểu đồ đưa vào báo cáo (matplotlib).

## 2. Tái lập baseline (bắt buộc để so sánh) — 🟡 FREE, cần GPU (khoảng 2–3 giờ)
- [x] 🟢 Viết `evaluate.py` với 5 metric như baseline. Chạy trên CPU được. → `scripts/evaluate.py` + `src/metrics.py` (test khớp công thức gốc).
- [ ] 🟡 Build FAISS index baseline: sbert, chunk 2000, khoảng 170k chunk, mất khoảng 20–40 phút trên T4. **Lưu index lại.**
- [ ] 🟡 Chạy baseline với **N ≥ 100** câu (ví dụ 200, cố định cùng một tập con, có seed). Qwen1.5-1.8B mất khoảng 30–60 phút.
- [ ] 🟢 Lưu `results/baseline_metrics.csv` và bảng trung bình 5 chỉ số.
- [x] 🟢 Sửa lỗi nhỏ nếu cần nhưng phải ghi chú. Ví dụ: baseline in ra `generated_text` có lặp lại prompt, → **Đã xác nhận trong mã nguồn LangChain:** output baseline có lẫn prompt. Có 2 chế độ `--llm baseline` / `baseline-noecho`.
  vì `HuggingFacePipeline` mặc định `return_full_text=True`. Kiểm tra lỗi này có làm thay đổi metric không.
- [x] 🟢 Tách sẵn một tập **eval cố định**. Nên gồm cả 51 câu có văn bản trong corpus cộng các câu ngẫu nhiên, và báo cáo kết quả riêng từng nhóm. → `data/eval_set.csv` (200 câu = 51 covered + 149 ngẫu nhiên, seed 42).

## 3. Cải tiến retrieval
- [x] 🟢 **Tiền xử lý:** chuẩn hóa Unicode (NFC), nối lại các dòng bị ngắt, bỏ header/footer lặp. Giữ chữ hoa/thường cho model embedding nếu model hỗ trợ.
- [x] 🟢 **Metadata:** lưu tên file, số hiệu, loại văn bản, năm, Điều/Khoản vào từng chunk. Baseline đang bỏ hết metadata.
- [x] 🟢 **Chunking theo cấu trúc pháp lý:** cắt theo "Điều …" với kích thước khoảng 500–1000 ký tự, overlap 100–200.
  Thêm tiêu đề văn bản và số hiệu vào đầu mỗi chunk.
- [x] 🟢 **BM25** (`rank_bm25` hoặc `bm25s`, tách từ bằng `pyvi` hoặc `underthesea`) chạy trên CPU. Nên dùng `bm25s` vì nhanh, đủ cho khoảng 500k chunk. → tự cài BM25 bằng scipy sparse (bm25s bị hết RAM), âm tiết + bigram, khoảng 2 phút cho 385k chunk.
- [x] 🟢 **Bắt số hiệu trong câu hỏi:** nếu câu hỏi có regex dạng `\d+/\d{4}/[A-ZĐ-]+`, ưu tiên hoặc lọc các chunk của văn bản đó.
- [ ] 🟡 **Embedding:** mỗi model cần build lại index (khoảng 20–60 phút cho model base, 2–4 giờ cho bge-m3). Để tiết kiệm quota, nên chọn 2–3 model:
  `bkai-foundation-models/vietnamese-bi-encoder`, `intfloat/multilingual-e5-base`, (`BAAI/bge-m3` nếu dư quota), so với `keepitreal/vietnamese-sbert`.
  Nhớ tách từ cho các model PhoBERT-based và dùng prefix `query:`/`passage:` cho e5.
  *Mẹo:* so sánh embedding trước trên **một tập con corpus** (ví dụ 2.000 file có liên quan) để chọn model, rồi mới embed toàn bộ.
- [x] 🟢 **Hybrid retrieval:** BM25 kết hợp dense, ghép bằng RRF hoặc trọng số. Phần ghép chạy trên CPU vì index dense đã có sẵn. → code xong (`src/retriever.py`), cần FAISS index (🟡) để chạy.
- [ ] 🟡 **Re-ranking:** cross-encoder như `BAAI/bge-reranker-v2-m3` hoặc `itdainb/PhoRanker`. Lấy top-20 rồi rerank xuống top 3–5.
  Mất vài giây mỗi câu trên GPU; CPU vẫn chạy được nhưng chậm.
- [ ] 🟡 (Tùy chọn) Query rewriting hoặc HyDE bằng chính LLM nhỏ. Cách này tốn thêm thời gian GPU cho mỗi câu hỏi. MMR (🟢) để giảm trùng lặp.
- [x] 🟢 Đánh giá riêng retrieval: Recall@k, MRR trên những câu có văn bản nguồn trong corpus. Phần này không cần LLM. → `results/retrieval/retrieval_summary.csv` (BM25).

## 4. Cải tiến generation — 🟡 FREE, cần GPU (phần tốn quota nhiều nhất)
- [ ] 🟡 Đổi sang LLM **instruct** dưới 4B, ví dụ `Qwen/Qwen2.5-3B-Instruct` (hoặc Qwen2.5-1.5B-Instruct, Llama-3.2-3B-Instruct).
  Dùng `apply_chat_template` và `return_full_text=False`. Tải model miễn phí; Llama cần bấm đồng ý license trên HF.
- [x] 🟢 **Prompt engineering:** prompt tiếng Việt, đóng vai luật sư, bắt trả lời theo mẫu
  *"Căn cứ tại Điều … [văn bản] quy định: …"*, trích nguyên văn điều luật liên quan. Đưa vào 1–2 ví dụ few-shot lấy từ tập train (không lấy từ tập eval).
  Viết và thử trên N=5–10 câu trước để đỡ tốn quota.
- [ ] 🟡 **Độ dài câu trả lời:** câu trả lời tham chiếu dài khoảng 1.600 ký tự (≈350 từ), nên tăng `max_new_tokens` lên 512–768 để tránh bị phạt brevity penalty BLEU.
  Lưu ý: câu trả lời dài hơn thì **sinh lâu hơn**, mỗi lần chạy tốn thêm quota. Đặt `repetition_penalty` khoảng 1.1.
- [x] 🟢 **Ghép context:** đánh số chunk, ghi nguồn (số hiệu, Điều), giới hạn tổng số token, đặt chunk liên quan nhất ở đầu hoặc cuối.
- [x] 🟢 Hậu xử lý: cắt phần lặp, bỏ các token đặc biệt.
- [ ] 🟡 (Tùy chọn) Dùng 4/8-bit (bitsandbytes) để chạy model 3B trên T4 hoặc chạy 2 model song song trên Kaggle T4×2. Có thể dùng `vLLM` để sinh nhanh hơn 3–5 lần.

## 5. Thí nghiệm và ablation (báo cáo, 3đ) — 🟡 FREE, cần GPU (khoảng 6–12 giờ, phần lớn quota)
- [x] 🟢 Dùng chung `evaluate.py`, cùng tập eval, cùng model embedding cho cosine.
  Cosine phải dùng **cùng embedding với baseline** để so sánh công bằng.
- [ ] 🟡 Bảng ablation, mỗi bước thay một thành phần:
  baseline → instruct LLM + prompt → chunking mới → embedding mới → hybrid → rerank → full.
  Khoảng 6 lần chạy × 1–2 giờ. Có thể chia ra 2 tuần quota Kaggle.
- [x] 🟢 **Cache** câu trả lời của mỗi cấu hình ra CSV. Tính lại metric và phân tích trên CPU, không phải chạy lại LLM. → `results/predictions/*.csv`, chạy tiếp được nếu bị ngắt.
- [~] 🟢 Ghi thời gian chạy và bộ nhớ GPU. → thời gian/câu đã ghi (`sec_per_q`), VRAM thì ghi tay khi chạy GPU.
- [ ] 🟢 Phân tích lỗi: vài ví dụ tốt/xấu, tách riêng nhóm có và không có văn bản trong corpus.

## 6. Demo (2đ) — 🟡 FREE, cần GPU khi chạy demo
- [x] 🟢 Notebook `demo.ipynb` hoặc app Gradio (free, `share=True` tạo link công khai 72 giờ): nhập câu hỏi → trả lời kèm nguồn (số hiệu, Điều, đoạn trích). → `app/demo.py` (CLI/Gradio) + `notebooks/demo.ipynb`. Đã test chế độ CPU `--llm extractive`.
- [x] 🟢 Chuẩn bị 5–10 câu hỏi mẫu, ưu tiên câu có văn bản nguồn trong corpus.
- [ ] 🟡 Đảm bảo chạy từ đầu đến cuối không lỗi. Load index đã lưu sẵn để demo nhanh, không phải build lại.
- [ ] 🟢 (Tùy chọn) Dự phòng: lưu sẵn output demo trong notebook, phòng khi lúc chấm không có GPU.
- [ ] 🔴 (Tùy chọn, không cần) Host demo cố định trên HuggingFace Spaces có GPU (trả phí theo giờ). Spaces CPU free thì quá chậm với model 3B.

## 7. Báo cáo và manual (5đ) — 🟢 FREE
- [~] 🟢 Báo cáo gồm: giới thiệu → khám phá dữ liệu → baseline → phương pháp → thí nghiệm, bảng và biểu đồ → phân tích → hạn chế (độ phủ corpus) → kết luận. → bản nháp `report/report.md` (đã có phần dữ liệu, phương pháp và kết quả CPU; chờ số liệu GPU).
  Viết bằng LaTeX/Overleaf (free) hoặc Word/Google Docs.
- [x] 🟢 `README`/manual: cài đặt (`requirements.txt`), tải và giải nén dữ liệu, build index, chạy evaluate, chạy demo, số cặp QA đã dùng, cấu hình GPU đã dùng. → `README.md`.
- [ ] 🟡 Kiểm tra lại toàn bộ quy trình trên môi trường sạch (một notebook Kaggle hoặc Colab mới).
- [ ] 🟢 Đóng gói nộp bài: source code, dataset (hoặc link), manual, báo cáo PDF.

---

### Gợi ý thứ tự làm (tối ưu quota GPU)
1. **🟢 Làm trên CPU trước:** 0 → 1 → viết `evaluate.py`, tiền xử lý, chunking, BM25, prompt (thử bằng vài câu).
2. **🟡 Phiên GPU 1:** build index baseline + chạy baseline N≥100 → có số để so sánh.
3. **🟡 Phiên GPU 2:** đổi LLM instruct + prompt mới (thường tăng điểm nhiều nhất, không cần build lại index).
4. **🟡 Phiên GPU 3–4:** build index mới (chunking và embedding mới) → hybrid → rerank → ablation.
5. **🟢 Hoàn thiện:** 6 → 7 (báo cáo, manual), chỉ cần GPU để kiểm tra lại lần cuối.
