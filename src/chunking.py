"""Chunking strategies (CPU only, no LangChain dependency).

* `baseline_chunks`  — reproduces the baseline: lowercase, newlines -> spaces, recursive character
  split with chunk_size=2000 / overlap=50 (same separators as LangChain's RecursiveCharacterTextSplitter).
* `legal_chunks`     — structure-aware: split on "Chương / Mục / Điều" headings, then pack paragraphs
  into ~CHUNK_SIZE character windows with overlap; every chunk is prefixed with a short header
  (document type, number, title, current Điều) so that it is self-contained for retrieval and for the LLM.
"""
import re

# ------------------------------------------------------------------ baseline (recursive splitter)
_SEPARATORS = ["\n\n", "\n", " ", ""]


def _split_recursive(text, size, overlap, seps):
    sep = seps[-1]
    rest = []
    for i, s in enumerate(seps):
        if s == "" or s in text:
            sep, rest = s, seps[i + 1:]
            break
    pieces = list(text) if sep == "" else text.split(sep)
    good, out = [], []
    for p in pieces:
        if len(p) < size:
            good.append(p)
        else:
            if good:
                out.extend(_merge(good, sep, size, overlap))
                good = []
            if rest:
                out.extend(_split_recursive(p, size, overlap, rest))
            else:
                out.append(p)
    if good:
        out.extend(_merge(good, sep, size, overlap))
    return out


def _merge(splits, sep, size, overlap):
    docs, cur, total = [], [], 0
    sl = len(sep)
    for s in splits:
        n = len(s)
        if total + n + (sl if cur else 0) > size and cur:
            doc = sep.join(cur).strip()
            if doc:
                docs.append(doc)
            while total > overlap or (total + n + (sl if cur else 0) > size and total > 0):
                total -= len(cur[0]) + (sl if len(cur) > 1 else 0)
                cur.pop(0)
        cur.append(s)
        total += n + (sl if len(cur) > 1 else 0)
    doc = sep.join(cur).strip()
    if doc:
        docs.append(doc)
    return docs


def baseline_chunks(raw_text, size=2000, overlap=50):
    content = raw_text.replace("\n", " ").lower().strip()
    return _split_recursive(content, size, overlap, _SEPARATORS)


# ------------------------------------------------------------------ structure-aware
HEADING_RE = re.compile(r"^(Chương\s+[IVXLC\d]+|CHƯƠNG\s+[IVXLC\d]+|Mục\s+\d+|MỤC\s+\d+|Điều\s+\d+[a-zđ]?)\b[.:]?\s*(.*)$")


def _pack(paras, size, overlap):
    """Greedy-pack paragraphs into windows of ~size chars; long paragraphs are split on sentences."""
    units = []
    for p in paras:
        if len(p) <= size:
            units.append(p)
        else:
            sents = re.split(r"(?<=[.;:])\s+", p)
            buf = ""
            for s in sents:
                while len(s) > size:          # pathological: no punctuation at all
                    units.append(s[:size]); s = s[size - overlap:]
                if len(buf) + len(s) + 1 > size and buf:
                    units.append(buf); buf = ""
                buf = (buf + " " + s).strip()
            if buf:
                units.append(buf)
    chunks, cur = [], []
    for u in units:
        if cur and sum(len(x) + 1 for x in cur) + len(u) > size:
            chunks.append("\n".join(cur))
            # overlap: keep trailing units up to `overlap` chars
            keep, tot = [], 0
            for x in reversed(cur):
                if tot + len(x) > overlap:
                    break
                keep.insert(0, x); tot += len(x)
            if not keep and overlap > 0:
                tail = cur[-1][-overlap:]
                keep = [tail.split(" ", 1)[-1] if " " in tail else tail]   # start on a word boundary
            cur = keep
        cur.append(u)
    if cur:
        chunks.append("\n".join(cur))
    return chunks


def legal_chunks(clean_text, meta, size=1000, overlap=150, min_chars=80):
    """Return a list of dicts {text, header, dieu, chuong} for one cleaned document."""
    paras = [p.strip() for p in clean_text.split("\n") if p.strip()]
    sections, cur, chuong, dieu = [], [], "", ""
    for p in paras:
        m = HEADING_RE.match(p)
        if m:
            kind = m.group(1).split()[0].lower()
            if cur:
                sections.append((chuong, dieu, cur))
            cur = [p]
            if kind == "chương":
                chuong, dieu = p[:120], ""
            elif kind == "điều":
                dieu = p[:160]
            continue
        cur.append(p)
    if cur:
        sections.append((chuong, dieu, cur))

    doc_label = " ".join(x for x in [meta.get("doc_type") or "", meta.get("doc_id") or ""] if x).strip()
    title = (meta.get("title") or "")[:220]
    if meta.get("doc_id") and meta["doc_id"] in title:   # crawled titles already contain type + number
        doc_label = ""
    out = []
    pending = None   # merge tiny sections (e.g. a heading alone) into the next one
    for chuong, dieu, ps in sections:
        if pending:
            ps = pending + ps
            pending = None
        if sum(len(p) for p in ps) < min_chars:
            pending = ps
            continue
        for body in _pack(ps, size, overlap):
            header = (f"[{doc_label}] {title}" if doc_label else f"[{title}]").strip()
            if dieu and not body.startswith(dieu[:20]):
                header += f" | {dieu}"
            out.append({"text": body, "header": header, "dieu": dieu, "chuong": chuong})
    if pending:
        body = "\n".join(pending)
        if out:
            out[-1]["text"] += "\n" + body
        else:
            out.append({"text": body, "header": (f"[{doc_label}] {title}" if doc_label else f"[{title}]").strip(),
                        "dieu": "", "chuong": ""})
    return out
