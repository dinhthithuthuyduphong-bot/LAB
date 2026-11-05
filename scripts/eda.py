"""Step 3 (CPU): data exploration for the report.

Needs data/corpus_meta.csv and data/res.csv.
Outputs figures + tables in results/eda/ and a markdown summary results/eda/eda_summary.md

Usage:  python -I scripts/eda.py
"""
import sys, re, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from src import config
from src.legal_text import normalize_doc_id

OUT = config.RESULTS_DIR / "eda"
plt.rcParams.update({"figure.dpi": 120, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.alpha": 0.3, "font.size": 9})
C1, C2 = "#2a6fdb", "#e07a2e"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name)
    plt.close(fig)


def year_of_ref(r):
    m = re.search(r"/((?:19|20)\d{2})/", r)
    return int(m.group(1)) if m else None


def question_type(q):
    ql = q.lower()
    if ql.startswith("có phải") or re.search(r"(có|không) (được|phải)\b.*\?$", ql) or ql.endswith("không?"):
        return "Có/Không"
    if re.search(r"bao nhiêu|mức|tỷ lệ|thời hạn|bao lâu|khi nào|ngày nào", ql):
        return "Số liệu / thời hạn"
    if re.search(r"như thế nào|thế nào|ra sao|quy định gì|những gì|gồm những|bao gồm", ql):
        return "Mô tả quy định"
    if re.search(r"ai |cơ quan nào|đơn vị nào|thẩm quyền", ql):
        return "Chủ thể / thẩm quyền"
    if re.search(r"điều kiện|hồ sơ|thủ tục|trình tự", ql):
        return "Điều kiện / thủ tục"
    return "Khác"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    meta = pd.read_csv(config.DATA_DIR / "corpus_meta.csv")
    res = pd.read_csv(config.RES_CSV)
    freq = pd.read_excel(config.RES_XLSX, sheet_name=1)
    S = {}

    # ---------------- Corpus ----------------
    S["corpus_docs"] = len(meta)
    S["corpus_chars"] = int(meta.chars.sum())
    S["corpus_chars_desc"] = meta.chars.describe(percentiles=[.25, .5, .75, .95]).round(0).to_dict()
    S["docs_with_dieu"] = int((meta.n_dieu > 0).sum())
    S["est_chunks_2000"] = int((meta.chars / 1950).clip(lower=1).round().sum())
    S["est_chunks_1000"] = int((meta.chars / 850).clip(lower=1).round().sum())

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.hist(meta.chars.clip(upper=100_000), bins=60, color=C1)
    ax.set(xlabel="Số ký tự / văn bản (cắt ở 100k)", ylabel="Số văn bản", title="Độ dài văn bản trong corpus")
    save(fig, "corpus_length.png")

    types = meta.doc_type.fillna("Không rõ").value_counts()
    top_types = types.head(10)
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.barh(top_types.index[::-1], top_types.values[::-1], color=C1)
    ax.set(xlabel="Số văn bản", title="Loại văn bản (top 10)")
    save(fig, "corpus_doc_types.png")
    S["doc_types"] = types.head(15).to_dict()

    issuers = meta.issuer.fillna("Không rõ").value_counts()
    S["issuers"] = issuers.head(15).to_dict()
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.barh(issuers.head(12).index[::-1], issuers.head(12).values[::-1], color=C1)
    ax.set(xlabel="Số văn bản", title="Cơ quan ban hành theo số hiệu (top 12)")
    save(fig, "corpus_issuers.png")

    fields = meta.field.fillna("Không rõ").str.split(",").explode().str.strip().value_counts()
    S["fields"] = fields.head(12).to_dict()
    S["status"] = meta.status.fillna("Không rõ").str.split(":").str[0].value_counts().head(6).to_dict()
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.barh(fields.head(10).index[::-1], fields.head(10).values[::-1], color=C1)
    ax.set(xlabel="Số văn bản (một văn bản có thể thuộc nhiều lĩnh vực)", title="Lĩnh vực văn bản (top 10)")
    save(fig, "corpus_fields.png")

    yrs = meta.year.dropna().astype(int)
    yrs = yrs[(yrs >= 1945) & (yrs <= 2026)]
    S["year_range"] = [int(yrs.min()), int(yrs.max())]

    # ---------------- QA ----------------
    res["q_words"] = res.question.str.split().str.len()
    res["a_words"] = res.answer.str.split().str.len()
    res["a_chars"] = res.answer.str.len()
    S["qa_pairs"] = len(res)
    S["q_words_desc"] = res.q_words.describe(percentiles=[.5, .95]).round(1).to_dict()
    S["a_words_desc"] = res.a_words.describe(percentiles=[.5, .95]).round(1).to_dict()
    S["a_chars_mean"] = round(res.a_chars.mean(), 1)
    S["answers_start_with_can_cu"] = round(res.answer.str.lower().str.startswith("căn cứ").mean(), 3)
    S["answers_mention_dieu"] = round(res.answer.str.contains(r"Điều \d", regex=True).mean(), 3)
    S["questions_mention_doc_id"] = round(res.question.str.contains(r"\d+/\d{4}/|\d+/[A-ZĐ]", regex=True).mean(), 3)
    S["unique_ref_docs"] = int(res.ref_norm.nunique())
    S["labelled_rows"] = int(res.answer_correct.notna().sum())

    fig, axs = plt.subplots(1, 2, figsize=(8, 3))
    axs[0].hist(res.q_words, bins=40, color=C1); axs[0].set(title="Độ dài câu hỏi", xlabel="số từ (âm tiết)", ylabel="Số câu")
    axs[1].hist(res.a_words.clip(upper=1000), bins=50, color=C2); axs[1].set(title="Độ dài câu trả lời tham chiếu", xlabel="số từ (cắt ở 1000)")
    save(fig, "qa_lengths.png")

    res["q_type"] = res.question.map(question_type)
    qt = res.q_type.value_counts()
    S["question_types"] = qt.to_dict()
    fig, ax = plt.subplots(figsize=(6, 2.8))
    ax.barh(qt.index[::-1], qt.values[::-1], color=C1)
    ax.set(xlabel="Số câu hỏi", title="Phân loại câu hỏi (heuristic theo từ khóa)")
    save(fig, "qa_question_types.png")

    ref_issuer = res.ref_doc.str.extract(r"-([A-ZĐa-z]+)$")[0].fillna("Khác")
    S["ref_issuers"] = ref_issuer.value_counts().head(12).to_dict()
    ref_type = res.ref_doc.str.extract(r"/(?:\d{4}/)?([A-ZĐa-z]+)-")[0].fillna("Khác")
    S["ref_types"] = ref_type.value_counts().head(10).to_dict()

    no_ref = res.ref_doc.str.lower().str.contains("không trích xuất")
    S["rows_without_ref"] = int(no_ref.sum())
    top_refs = res[~no_ref].ref_doc.value_counts().head(15)
    fig, ax = plt.subplots(figsize=(6, 3.6))
    known = set(meta.doc_id_norm) | set(meta.file_doc_id_norm)
    colors = [C2 if normalize_doc_id(r) in known else C1 for r in top_refs.index]
    ax.barh(top_refs.index[::-1], top_refs.values[::-1], color=colors[::-1])
    ax.set(xlabel="Số câu hỏi", title="Văn bản được hỏi nhiều nhất (cam = có trong corpus)")
    save(fig, "qa_top_refs.png")

    # ---------------- Coverage / mismatch ----------------
    cov = res.groupby("ref_norm").agg(n=("id", "size"), in_corpus=("in_corpus", "first")).reset_index()
    S["coverage_rows"] = int(res.in_corpus.sum())
    S["coverage_docs"] = int(cov.in_corpus.sum())
    S["covered_docs"] = cov[cov.in_corpus].sort_values("n", ascending=False)[["ref_norm", "n"]].values.tolist()

    # Which corpus files match the covered refs (a local number like 1590/QĐ-UBND can be ambiguous)
    amb = {}
    for r in cov[cov.in_corpus].ref_norm:
        m = meta[(meta.doc_id_norm == r) | (meta.file_doc_id_norm == r)]
        amb[r] = m[["file", "year", "title"]].to_dict("records")
    (OUT / "covered_docs_matches.json").write_text(json.dumps(amb, ensure_ascii=False, indent=1), encoding="utf-8")

    qa_years = res.ref_doc.map(year_of_ref).dropna().astype(int)
    S["qa_ref_year_median"] = int(qa_years.median())
    fig, ax = plt.subplots(figsize=(7, 3))
    bins = range(1990, 2027)
    ax.hist(yrs[yrs >= 1990], bins=bins, color=C1, alpha=.7, density=True, label="Corpus (năm ban hành)")
    ax.hist(qa_years[qa_years >= 1990], bins=bins, color=C2, alpha=.7, density=True, label="Văn bản được hỏi trong RES")
    ax.set(xlabel="Năm", ylabel="Tỷ lệ", title="Lệch phân bố năm: corpus vs câu hỏi")
    ax.legend()
    save(fig, "year_mismatch.png")

    # Keyword topic comparison: banking vocabulary in questions vs corpus
    kw = ["ngân hàng", "tín dụng", "lao động", "tiền lương", "bảo hiểm", "đất đai", "thuế", "giáo dục"]
    docs_text = [json.loads(l)["text"][:20000].lower() for l in open(config.ARTIFACTS_DIR / "docs.jsonl", encoding="utf-8")]
    topic = []
    for k in kw:
        topic.append({"keyword": k,
                      "pct_questions": round(100 * res.question.str.lower().str.contains(k).mean(), 1),
                      "pct_corpus_docs": round(100 * sum(k in d for d in docs_text) / len(docs_text), 1)})
    topic = pd.DataFrame(topic)
    topic.to_csv(OUT / "topic_keywords.csv", index=False)
    S["topic_keywords"] = topic.to_dict("records")
    fig, ax = plt.subplots(figsize=(7, 3))
    x = range(len(kw))
    ax.bar([i - .2 for i in x], topic.pct_questions, .4, color=C2, label="% câu hỏi")
    ax.bar([i + .2 for i in x], topic.pct_corpus_docs, .4, color=C1, label="% văn bản corpus")
    ax.set_xticks(list(x)); ax.set_xticklabels(kw, rotation=20)
    ax.set(ylabel="%", title="Chủ đề: câu hỏi vs corpus"); ax.legend()
    save(fig, "topic_mismatch.png")

    S["citation_freq_sheet_top10"] = freq.head(10)[["Số hiệu Văn bản", "Số lần xuất hiện"]].values.tolist()

    (OUT / "eda_stats.json").write_text(json.dumps(S, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    write_md(S)
    print(json.dumps(S, ensure_ascii=False, indent=1, default=str)[:4000])


def write_md(S):
    t = S["topic_keywords"]
    md = f"""# Khám phá dữ liệu (EDA)

*Sinh tự động bởi `scripts/eda.py`. Hình nằm trong `results/eda/`.*

## Corpus văn bản pháp luật
- **{S['corpus_docs']:,} văn bản**, tổng **{S['corpus_chars']:,} ký tự** sau khi làm sạch. Năm ban hành từ {S['year_range'][0]} đến {S['year_range'][1]}.
- Độ dài văn bản: trung vị {S['corpus_chars_desc']['50%']:,.0f} ký tự, p95 {S['corpus_chars_desc']['95%']:,.0f}, dài nhất {S['corpus_chars_desc']['max']:,.0f}.
- {S['docs_with_dieu']:,} văn bản có cấu trúc "Điều …", nên có thể chunk theo Điều.
- Ước lượng số chunk: khoảng {S['est_chunks_2000']:,} với chunk 2000 ký tự (baseline), khoảng {S['est_chunks_1000']:,} với chunk 1000/150.
- Loại văn bản nhiều nhất: {', '.join(f'{k} ({v})' for k, v in list(S['doc_types'].items())[:6])}.
- Cơ quan ban hành nhiều nhất: {', '.join(f'{k} ({v})' for k, v in list(S['issuers'].items())[:6])}.
- **Lĩnh vực** (từ khối metadata "THÔNG TIN THÊM" ở cuối mỗi file): {', '.join(f'{k} ({v})' for k, v in list(S['fields'].items())[:6])}.
- Tình trạng hiệu lực: {', '.join(f'{k} ({v})' for k, v in S['status'].items())}.
- Mỗi file kết thúc bằng 3 khối do crawler thêm vào: "THÔNG TIN THÊM" (metadata), "MỤC LỤC" và "VĂN BẢN LIÊN QUAN".
  Khi tiền xử lý, metadata được tách ra làm trường riêng, còn hai khối sau bị loại vì là nhiễu: mục lục lặp lại nội dung, còn danh sách liên kết thì không liên quan.

![](corpus_length.png) ![](corpus_doc_types.png) ![](corpus_issuers.png) ![](corpus_fields.png)

## Bộ câu hỏi RES
- **{S['qa_pairs']:,} cặp QA**, trích dẫn {S['unique_ref_docs'] - 1} văn bản khác nhau; **{S['rows_without_ref']} câu (28%) không có số hiệu** ("Không trích xuất được"). Chỉ {S['labelled_rows']} dòng có nhãn đúng/sai.
- Câu hỏi: trung bình {S['q_words_desc']['mean']} từ. Câu trả lời: trung bình **{S['a_words_desc']['mean']} từ** ({S['a_chars_mean']:,} ký tự), p95 {S['a_words_desc']['95%']} từ.
- {S['answers_start_with_can_cu']*100:.0f}% câu trả lời bắt đầu bằng "Căn cứ…", và {S['answers_mention_dieu']*100:.0f}% có nhắc "Điều N".
  Mẫu câu này nên dùng cho prompt.
- {S['questions_mention_doc_id']*100:.0f}% câu hỏi có ghi số hiệu văn bản ngay trong câu, nên có thể dùng regex để lọc hoặc ưu tiên văn bản đó khi retrieve.
- Loại câu hỏi (heuristic): {', '.join(f'{k} {v}' for k, v in S['question_types'].items())}.
- Cơ quan của văn bản được hỏi: {', '.join(f'{k} ({v})' for k, v in list(S['ref_issuers'].items())[:6])}.
  Phần lớn là văn bản **ngân hàng (NHNN)** và Nghị định của Chính phủ.

![](qa_lengths.png) ![](qa_question_types.png) ![](qa_top_refs.png)

## ⚠️ Độ phủ: corpus không khớp với câu hỏi
- Chỉ **{S['coverage_docs']}/{S['unique_ref_docs'] - 1}** văn bản được hỏi có trong corpus, ứng với **{S['coverage_rows']}/{S['qa_pairs']}** câu hỏi ({S['coverage_rows']/S['qa_pairs']*100:.1f}%).
- Các văn bản có trong corpus: {', '.join(f'{d} ({n} câu)' for d, n in S['covered_docs'])}.
  Lưu ý: số hiệu địa phương (vd `…/QĐ-UBND`) có thể trùng giữa các tỉnh. Xem `covered_docs_matches.json`.
- Năm của văn bản được hỏi có trung vị {S['qa_ref_year_median']}, nghiêng hẳn về 2024–2025, trong khi corpus trải dài từ {S['year_range'][0]}.
- Chủ đề lệch nhau: "ngân hàng" xuất hiện trong {t[0]['pct_questions']}% câu hỏi nhưng chỉ {t[0]['pct_corpus_docs']}% văn bản;
  ngược lại, "lao động" xuất hiện trong {t[2]['pct_questions']}% câu hỏi nhưng có mặt trong {t[2]['pct_corpus_docs']}% văn bản.
  Nói cách khác, corpus chủ yếu là văn bản về **lao động, tiền lương, việc làm**, còn câu hỏi chủ yếu về **ngân hàng**.

![](year_mismatch.png) ![](topic_mismatch.png)

**Hệ quả cho thiết kế:**
1. Retrieval chỉ có thể tìm đúng văn bản nguồn cho khoảng 2% câu hỏi. Với phần còn lại, nó chỉ tìm được văn bản *liên quan về chủ đề*.
   Vì vậy kết quả được báo cáo riêng cho hai nhóm `covered` và `not_covered`.
2. Metric đo bằng độ trùng từ với câu trả lời tham chiếu dài khoảng {S['a_words_desc']['mean']:.0f} từ, nên **dạng và độ dài** câu trả lời
   (mở đầu "Căn cứ…", trích Điều, đủ dài để không bị phạt brevity penalty) ảnh hưởng rất lớn tới điểm.
3. LLM phải được dặn **không bịa số hiệu hay điều luật** khi ngữ cảnh không chứa văn bản được hỏi.
"""
    (OUT / "eda_summary.md").write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()
