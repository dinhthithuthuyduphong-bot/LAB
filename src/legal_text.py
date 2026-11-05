"""Text normalisation and metadata extraction for Vietnamese legal documents (CPU only)."""
import re
import unicodedata

# Document number such as 50/2024/TT-NHNN, 1590/QĐ-UBND, 01/2005/TTLT-BCA-BLĐTBXH
DOC_ID_RE = re.compile(
    r"\b(\d{1,5}[a-zA-Z]?(?:/\d{4})?/[A-ZĐ][A-ZĐa-zđ0-9]*(?:[-–][A-ZĐ][A-ZĐa-zđ0-9]*)*)"
)

DOC_TYPES = {
    "LUẬT": "Luật", "BỘ LUẬT": "Bộ luật", "NGHỊ ĐỊNH": "Nghị định", "THÔNG TƯ LIÊN TỊCH": "Thông tư liên tịch",
    "THÔNG TƯ LIÊN BỘ": "Thông tư liên bộ", "THÔNG TƯ": "Thông tư", "QUYẾT ĐỊNH": "Quyết định",
    "NGHỊ QUYẾT": "Nghị quyết", "CHỈ THỊ": "Chỉ thị", "CÔNG VĂN": "Công văn", "KẾ HOẠCH": "Kế hoạch",
    "THÔNG BÁO": "Thông báo", "PHÁP LỆNH": "Pháp lệnh", "HƯỚNG DẪN": "Hướng dẫn", "CHƯƠNG TRÌNH": "Chương trình",
}

# Mapping between the abbreviation inside a document number and its type
ABBR_TO_TYPE = {
    "NĐ": "Nghị định", "TT": "Thông tư", "TTLT": "Thông tư liên tịch", "QĐ": "Quyết định", "NQ": "Nghị quyết",
    "CT": "Chỉ thị", "KH": "Kế hoạch", "TB": "Thông báo", "CV": "Công văn", "HD": "Hướng dẫn", "L": "Luật",
    "QH": "Luật", "PL": "Pháp lệnh", "CTr": "Chương trình",
}


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


INFO_MARK = "--- THÔNG TIN THÊM ---"
INFO_KEYS = {"Ten": "info_title", "So hieu": "info_doc_id", "Loai van ban": "info_type", "Linh vuc nganh": "info_field",
             "Noi ban hanh": "info_issuer", "Nguoi ky": "info_signer", "Ngay ban hanh": "info_date",
             "Ngay hieu luc": "info_effective", "Tinh trang": "info_status"}


def split_info_block(raw: str):
    """Every corpus file ends with a crawled metadata block:
        --- THÔNG TIN THÊM ---  (Ten, So hieu, Loai van ban, Linh vuc nganh, Noi ban hanh, Ngay ban hanh, ...)
        --- MỤC LỤC ---         (table of contents, duplicates the body)
        --- VĂN BẢN LIÊN QUAN --- (links to other documents)
    Returns (body, info_dict). The trailing blocks are removed from the body (they are noise for retrieval)."""
    raw = nfc(raw)
    i = raw.find(INFO_MARK)
    if i < 0:
        j = raw.find("--- MỤC LỤC ---")
        j = j if j >= 0 else raw.find("--- VĂN BẢN LIÊN QUAN ---")
        return (raw[:j] if j >= 0 else raw), {}
    body, tail = raw[:i], raw[i + len(INFO_MARK):]
    tail = re.split(r"\n--- (?:MỤC LỤC|VĂN BẢN LIÊN QUAN) ---", tail)[0]
    info = {}
    for line in tail.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            if k in INFO_KEYS:
                v = v.strip()
                info[INFO_KEYS[k]] = None if (not v or v.startswith("Dữ liệu đang cập nhật")) else v
    return body, info


def clean_text(raw: str) -> str:
    """Normalise a raw corpus file (body only; the crawled metadata blocks are dropped).

    The corpus is hard-wrapped: a single newline breaks a sentence (e.g. "VIỆT\\n NAM"), while a blank
    line separates paragraphs. We join wrapped lines, keep paragraphs and keep case (case helps
    cased embedding models and makes the context easier for the LLM to quote).
    """
    body, _ = split_info_block(raw)
    t = body.replace("\r\n", "\n").replace("\r", "\n").replace("\u00a0", " ").replace("\ufeff", "")
    t = re.sub(r"[ \t]+", " ", t)
    paras = re.split(r"\n\s*\n", t)
    out = []
    for p in paras:
        p = re.sub(r"\s*\n\s*", " ", p).strip()
        if not p or re.fullmatch(r"[-_*=. ]+", p):   # separator lines such as "-------" or "******"
            continue
        out.append(p)
    return "\n".join(out)


def doc_id_from_filename(fname: str) -> str:
    """'01_2005_QĐ-UB_1.txt' -> '01/2005/QĐ-UB' (the _1/_2 suffix marks duplicate names)."""
    stem = nfc(fname).rsplit(".", 1)[0]
    stem = re.sub(r"_\d{1,2}$", "", stem)
    return stem.replace("_", "/")


def normalize_doc_id(s: str) -> str:
    """Canonical form used to compare document numbers coming from different sources."""
    s = nfc(str(s)).upper().strip()
    s = s.replace("–", "-").replace(" ", "").replace("_", "/")
    s = re.sub(r"/+", "/", s)
    return s


def extract_header_id(text: str):
    """Document number written in the header ('Số: 1590/QĐ-UBND')."""
    m = re.search(r"Số\s*(?:hiệu)?\s*[:.]\s*([0-9][^\s,;]*)", text[:1500])
    return m.group(1).strip(" .") if m else None


def extract_metadata(fname: str, text: str, info: dict = None) -> dict:
    """Metadata from the crawled info block when available, otherwise heuristics on the header."""
    info = info or {}
    head = text[:2500]
    doc_id = extract_header_id(head) or doc_id_from_filename(fname)
    year = None
    m = re.search(r"ngày\s+\d{1,2}\s+tháng\s+\d{1,2}\s+năm\s+(\d{4})", head)
    if m:
        year = int(m.group(1))
    else:
        m = re.search(r"/((?:19|20)\d{2})/", doc_id_from_filename(fname))
        if m:
            year = int(m.group(1))
    doc_type = None
    for k, v in DOC_TYPES.items():
        if re.search(r"(^|\n)\s*" + k + r"\b", head):
            doc_type = v
            break
    if doc_type is None:
        abbr = re.search(r"/(?:\d{4}/)?([A-ZĐa-z]+)", doc_id_from_filename(fname))
        if abbr:
            doc_type = ABBR_TO_TYPE.get(abbr.group(1), abbr.group(1))
    issuer = None
    m = re.search(r"[-–]([A-ZĐ][A-ZĐa-z0-9-]*)$", doc_id_from_filename(fname))
    if m:
        issuer = m.group(1)
    # Title: first ALL-CAPS paragraph after the document type heading
    title = ""
    lines = head.split("\n")
    for i, ln in enumerate(lines):
        if doc_type and ln.strip().upper().startswith(doc_type.upper()):
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            title = (ln.strip() + " " + nxt).strip() if len(ln.strip()) < 25 else ln.strip()
            break
    if info.get("info_doc_id"):
        doc_id = info["info_doc_id"]
    if info.get("info_type"):
        doc_type = info["info_type"]
    m = re.search(r"(\d{4})$", info.get("info_date") or "")
    if m:
        year = int(m.group(1))
    if info.get("info_title"):
        title = info["info_title"]
    return {
        "file": fname,
        "doc_id": doc_id,
        "doc_id_norm": normalize_doc_id(doc_id),
        "file_doc_id_norm": normalize_doc_id(doc_id_from_filename(fname)),
        "year": year,
        "doc_type": doc_type,
        "issuer": issuer,
        "title": title[:300],
        "field": info.get("info_field"),
        "issuer_name": info.get("info_issuer"),
        "date": info.get("info_date"),
        "status": info.get("info_status"),
    }


def find_doc_ids(text: str):
    """Document numbers mentioned in a question, normalised."""
    return [normalize_doc_id(x) for x in DOC_ID_RE.findall(nfc(text))]
