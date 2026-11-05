# TODO – RAG Law Chatbot (cải tiến so với Baseline)

Nguồn: `doc/RAG_Assignment.pdf`, `doc/Baseline.ipynb`, `doc/RES.xlsx`, `Dataset/export_1/`.

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

## 0. Môi trường và cấu trúc dự án
- [ ] Chọn nơi chạy: Colab có GPU (T4/L4) hoặc máy local. Ghi lại cấu hình.
- [ ] Tạo cấu trúc: `src/` (code), `notebooks/`, `results/`, `report/`, `requirements.txt`.
- [ ] Chuyển `RES.xlsx` sheet 1 thành `res.csv` để không phụ thuộc Google Sheet như baseline.
- [ ] Gom các tham số (đường dẫn, model, chunk size, k, số câu hỏi N) vào một file config.
- [ ] Đặt `seed` và generation deterministic (`do_sample=False`) để kết quả lặp lại được.
- [ ] Cân nhắc gỡ `Dataset/` khỏi git (442MB) và chỉ hướng dẫn cách tải/giải nén trong manual.

## 1. Khám phá dữ liệu (báo cáo, 1đ)
- [ ] Thống kê corpus: số file, phân bố độ dài, loại văn bản (QĐ, TT, NĐ, NQ, CT…), cơ quan ban hành, năm.
- [ ] Thống kê QA: độ dài câu hỏi và câu trả lời, phân bố chủ đề và văn bản được trích dẫn (dùng sheet 2), các mẫu câu hỏi.
- [ ] Đo **độ phủ**: bao nhiêu câu hỏi có văn bản nguồn nằm trong corpus (hiện tại là 51/2.745). Kiểm tra lại bằng cả tên file lẫn nội dung.
- [ ] Phân tích cấu trúc văn bản (Chương / Mục / Điều / Khoản / Điểm) để thiết kế cách chunk.
- [ ] Vẽ biểu đồ đưa vào báo cáo.

## 2. Tái lập baseline (bắt buộc để so sánh)
- [ ] Chạy baseline đúng như notebook, nhưng với **N ≥ 100** câu (ví dụ 200, cố định cùng một tập con, có seed).
- [ ] Lưu `results/baseline_metrics.csv` và bảng trung bình 5 chỉ số.
- [ ] Sửa lỗi nhỏ nếu cần nhưng phải ghi chú. Ví dụ: baseline in ra `generated_text` có lặp lại prompt,
  vì `HuggingFacePipeline` mặc định `return_full_text=True`. Kiểm tra lỗi này có làm thay đổi metric không.
- [ ] Tách sẵn một tập **eval cố định**. Nên gồm cả 51 câu có văn bản trong corpus cộng các câu ngẫu nhiên, và báo cáo kết quả riêng từng nhóm.

## 3. Cải tiến retrieval
- [ ] **Tiền xử lý:** chuẩn hóa Unicode (NFC), nối lại các dòng bị ngắt, bỏ header/footer lặp. Giữ chữ hoa/thường cho model embedding nếu model hỗ trợ.
- [ ] **Metadata:** lưu tên file, số hiệu, loại văn bản, năm, Điều/Khoản vào từng chunk. Baseline đang bỏ hết metadata.
- [ ] **Chunking theo cấu trúc pháp lý:** cắt theo "Điều …" với kích thước khoảng 500–1000 ký tự, overlap 100–200.
  Thêm tiêu đề văn bản và số hiệu vào đầu mỗi chunk.
- [ ] **Embedding:** thử và so sánh `bkai-foundation-models/vietnamese-bi-encoder`, `BAAI/bge-m3`,
  `intfloat/multilingual-e5-base/large` và `dangvantuan/vietnamese-embedding` với `keepitreal/vietnamese-sbert`.
  Nhớ tách từ (word-segment) cho các model PhoBERT-based và dùng prefix `query:`/`passage:` cho e5.
- [ ] **Hybrid retrieval:** BM25 (trên văn bản đã tách từ) kết hợp dense, ghép bằng RRF hoặc trọng số.
- [ ] **Bắt số hiệu trong câu hỏi:** nếu câu hỏi có regex dạng `\d+/\d{4}/[A-ZĐ-]+`, ưu tiên hoặc lọc các chunk của văn bản đó.
- [ ] **Re-ranking:** cross-encoder như `BAAI/bge-reranker-v2-m3` hoặc `itdainb/PhoRanker`. Lấy top-20 rồi rerank xuống top 3–5.
- [ ] (Tùy chọn) Query rewriting hoặc HyDE bằng chính LLM nhỏ. MMR để giảm trùng lặp.
- [ ] Đánh giá riêng retrieval: Recall@k, MRR trên những câu có văn bản nguồn trong corpus.

## 4. Cải tiến generation
- [ ] Đổi sang LLM **instruct** dưới 4B, ví dụ `Qwen/Qwen2.5-3B-Instruct` (hoặc Qwen2.5-1.5B-Instruct, Llama-3.2-3B-Instruct, Vistral/SeaLLM nếu đủ nhỏ).
  Dùng `apply_chat_template` và `return_full_text=False`.
- [ ] **Prompt engineering:** prompt tiếng Việt, đóng vai luật sư, bắt trả lời theo mẫu
  *"Căn cứ tại Điều … [văn bản] quy định: …"*, trích nguyên văn điều luật liên quan. Đưa vào 1–2 ví dụ few-shot lấy từ tập train (không lấy từ tập eval).
- [ ] **Độ dài câu trả lời:** câu trả lời tham chiếu dài khoảng 1.600 ký tự (≈350 từ), nên tăng `max_new_tokens` lên 512–768 để tránh bị phạt brevity penalty BLEU. Đặt `repetition_penalty` khoảng 1.1.
- [ ] **Ghép context:** đánh số chunk, ghi nguồn (số hiệu, Điều), giới hạn tổng số token, đặt chunk liên quan nhất ở đầu hoặc cuối.
- [ ] Hậu xử lý: cắt phần lặp, bỏ các token đặc biệt.
- [ ] (Tùy chọn) Dùng quantization 4/8-bit để chạy model 3B trên T4.

## 5. Thí nghiệm và ablation (báo cáo, 3đ)
- [ ] Viết script `evaluate.py` dùng chung 5 metric như baseline, với cùng tập eval và cùng model embedding cho cosine.
  Cosine phải dùng **cùng embedding với baseline** để so sánh công bằng.
- [ ] Bảng ablation, mỗi bước thay một thành phần:
  baseline → instruct LLM + prompt → chunking mới → embedding mới → hybrid → rerank → full.
- [ ] Ghi thời gian chạy và bộ nhớ GPU.
- [ ] Phân tích lỗi: vài ví dụ tốt/xấu, tách riêng nhóm có và không có văn bản trong corpus.

## 6. Demo (2đ)
- [ ] Notebook `demo.ipynb` hoặc app Gradio/Streamlit: nhập câu hỏi → trả lời kèm nguồn (số hiệu, Điều, đoạn trích).
- [ ] Chuẩn bị 5–10 câu hỏi mẫu, ưu tiên câu có văn bản nguồn trong corpus.
- [ ] Đảm bảo chạy từ đầu đến cuối không lỗi. Có thể lưu sẵn FAISS index để demo nhanh.

## 7. Báo cáo và manual (5đ)
- [ ] Báo cáo gồm: giới thiệu → khám phá dữ liệu → baseline → phương pháp → thí nghiệm, bảng và biểu đồ → phân tích → hạn chế (độ phủ corpus) → kết luận.
- [ ] `README`/manual: cài đặt (`requirements.txt`), tải và giải nén dữ liệu, build index, chạy evaluate, chạy demo, số cặp QA đã dùng.
- [ ] Kiểm tra lại toàn bộ quy trình trên môi trường sạch.
- [ ] Đóng gói nộp bài: source code, dataset (hoặc link), manual, báo cáo PDF.

---

### Gợi ý thứ tự làm
1 → 2 (có số baseline sớm) → 4 (đổi LLM và prompt, thường tăng điểm nhiều nhất) → 3 → 5 → 6 → 7.
