"""Prompt construction (CPU only).

* `baseline_prompt`  — exact prompt of doc/Baseline.ipynb (for reproduction).
* `build_messages`   — improved chat prompt for instruct models: legal-assistant role, numbered sources,
  answer template that mirrors the reference answers ("Căn cứ tại … quy định: …"), anti-hallucination rules,
  optional few-shot example(s) taken ONLY from data/fewshot_pool.csv.
"""

BASELINE_TEMPLATE = """
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
{context}

Câu hỏi: {question}
Trả lời ngắn gọn và chính xác nhất có thể:
"""


def baseline_prompt(question, chunks):
    context = "\n".join(c["text"] if isinstance(c, dict) else str(c) for c in chunks)
    return BASELINE_TEMPLATE.format(context=context, question=question)


SYSTEM_PROMPT = """Bạn là luật sư tư vấn pháp luật Việt Nam. Bạn trả lời câu hỏi bằng tiếng Việt, dựa trên các trích đoạn văn bản pháp luật được cung cấp.

Quy tắc:
1. Mở đầu câu trả lời bằng căn cứ pháp lý theo mẫu: "Căn cứ tại [Điều/khoản/điểm] [loại văn bản] [số hiệu] quy định:" rồi trích hoặc diễn giải sát nội dung quy định.
2. Sau phần trích dẫn, trả lời thẳng vào câu hỏi. Nếu câu hỏi có nhiều ý thì trả lời đủ từng ý, dùng gạch đầu dòng "-" và "+" khi liệt kê.
3. Giữ nguyên thuật ngữ, con số, thời hạn, tỷ lệ như trong văn bản.
4. Chỉ dùng thông tin trong các trích đoạn. Không bịa số hiệu văn bản, số Điều hay con số.
   Nếu trích đoạn không chứa văn bản được hỏi, hãy nói rõ là không tìm thấy quy định cụ thể trong tài liệu, rồi nêu những quy định liên quan nhất mà trích đoạn có.
5. Câu trả lời đầy đủ nhưng không lặp lại ý, khoảng 150–400 từ."""


def format_context(chunks, max_chars=6000):
    """Numbered sources with their header (document number + Điều); truncated to a char budget."""
    parts, used = [], 0
    for i, c in enumerate(chunks, 1):
        head = c.get("header") or c.get("doc_id") or ""
        st = c.get("status") or ""
        if st.startswith(("Hết hiệu lực", "Không còn phù hợp")):
            head += f" (Tình trạng: {st})"
        body = c["text"]
        block = f"[Nguồn {i}] {head}\n{body}"
        if used + len(block) > max_chars:
            remain = max_chars - used - len(head) - 20
            if remain < 200:
                break
            block = f"[Nguồn {i}] {head}\n{body[:remain]}…"
        parts.append(block)
        used += len(block)
    return "\n\n".join(parts)


def _example_turns(examples, max_answer_chars=1200):
    turns = []
    for ex in examples:
        turns.append({"role": "user", "content": f"Câu hỏi: {ex['question']}"})
        ans = ex["answer"]
        if len(ans) > max_answer_chars:
            ans = ans[:max_answer_chars].rsplit(" ", 1)[0] + " …"
        turns.append({"role": "assistant", "content": ans})
    return turns


def build_messages(question, chunks, examples=(), max_context_chars=6000, qa_memory=()):
    """Chat messages for `tokenizer.apply_chat_template`.

    examples  – few-shot QA pairs (dicts with question/answer) shown as previous turns (style only)
    qa_memory – optional related QA pairs from the pool given as extra *reference material* (ablation only;
                must never contain eval questions)
    """
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
    msgs += _example_turns(examples)
    ctx = format_context(chunks, max_context_chars)
    extra = ""
    if qa_memory:
        extra = "\n\nHỏi đáp pháp lý tham khảo (có thể liên quan):\n" + "\n\n".join(
            f"- Hỏi: {m['question']}\n  Đáp: {m['answer'][:1500]}" for m in qa_memory)
    user = (f"Các trích đoạn văn bản pháp luật:\n{ctx}{extra}\n\n"
            f"Câu hỏi: {question}\n\n"
            "Hãy trả lời theo đúng các quy tắc đã nêu.")
    msgs.append({"role": "user", "content": user})
    return msgs


def messages_to_text(msgs):
    """Fallback plain-text rendering (for logging or for models without a chat template)."""
    return "\n\n".join(f"<{m['role']}>\n{m['content']}" for m in msgs)
