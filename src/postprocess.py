"""Clean LLM outputs (CPU only)."""
import re


def strip_prompt_echo(text, prompt):
    """Base models / HuggingFacePipeline(return_full_text=True) echo the prompt — remove it."""
    if prompt and text.startswith(prompt):
        return text[len(prompt):]
    return text


def remove_repetition(text, min_len=40):
    """Cut the answer when a sentence/line repeats (common with small models)."""
    seen, out = set(), []
    for line in re.split(r"(?<=[.\n])", text):
        key = re.sub(r"\s+", " ", line).strip().lower()
        if len(key) >= min_len and key in seen:
            break
        seen.add(key)
        out.append(line)
    return "".join(out)


def clean_answer(text, prompt=None):
    t = strip_prompt_echo(text or "", prompt)
    t = re.sub(r"<\|.*?\|>", "", t)                 # special tokens such as <|im_end|>
    t = re.split(r"\n\s*(?:Câu hỏi|Question|<user>|Human)\s*:", t)[0]  # model starts a new turn
    t = remove_repetition(t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()
