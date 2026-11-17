"""Demo: ask a legal question, get an answer with its sources.

  python -I app/demo.py                       # Gradio UI (GPU recommended)  -> share link printed
  python -I app/demo.py --cli "Mức lương cơ sở hiện nay là bao nhiêu?"
  python -I app/demo.py --llm extractive --retriever bm25_legal --cli "..."   # CPU only, no LLM (shows retrieval)
"""
import sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from src import config
from src.postprocess import clean_answer
from src.prompts import build_messages
from src.retriever import Retriever
from eval_retrieval import CONFIGS

EXAMPLES = [
    "Mức lương cơ sở áp dụng từ ngày 01/7/2024 đối với cán bộ, công chức, viên chức là bao nhiêu?",
    "Năm 2025 công chức, viên chức được nghỉ Tết Âm lịch bao nhiêu ngày, từ ngày nào đến ngày nào?",
    "Người lao động được nghỉ lễ, tết những ngày nào theo Bộ luật Lao động?",
    "Chế độ tiền thưởng theo Nghị định 73/2024/NĐ-CP được thực hiện như thế nào?",
    "Điều kiện cấp giấy phép lao động cho người nước ngoài làm việc tại Việt Nam là gì?",
]


class Bot:
    def __init__(self, retriever="bm25_legal", llm=config.LLM_MODEL, top_k=config.TOP_K, load_in_4bit=False):
        self.retr = Retriever(CONFIGS[retriever])
        self.top_k = top_k
        self.llm = None
        if llm != "extractive":
            from src.llm import HFChatLLM
            self.llm = HFChatLLM(llm, max_new_tokens=config.MAX_NEW_TOKENS, load_in_4bit=load_in_4bit)
        from src.fewshot import ExamplePool
        self.examples = ExamplePool().static(1)

    def answer(self, question):
        hits = self.retr.retrieve(question, top_k=self.top_k)
        if self.llm is None:
            ans = "(chế độ không dùng LLM: hiển thị đoạn liên quan nhất)\n\n" + (hits[0]["text"] if hits else "")
        else:
            msgs = build_messages(question, hits, examples=self.examples, max_context_chars=config.MAX_CONTEXT_CHARS)
            ans = clean_answer(self.llm.generate([msgs])[0][0])
        src = "\n".join(f"**[{i}]** {h['header'] or h['doc_id']} — `{h['file']}`\n> {h['text'][:300]}…"
                        for i, h in enumerate(hits, 1))
        return ans, src


def build_ui(bot):
    """Gradio UI. Errors are shown in the page and printed, instead of a silent endless spinner."""
    import traceback
    import gradio as gr

    def ask(q):
        if not q or not q.strip():
            return "Hãy nhập câu hỏi.", ""
        try:
            return bot.answer(q.strip())
        except Exception:
            err = traceback.format_exc()
            print(err, flush=True)
            return "**Lỗi:**\n```\n" + err[-2000:] + "\n```", ""

    with gr.Blocks(title="Chatbot pháp luật (RAG)") as ui:
        gr.Markdown("## Chatbot hỏi đáp pháp luật lao động – tiền lương (RAG)\n"
                    "Corpus: 16.439 văn bản lĩnh vực *Lao động – Tiền lương*. Câu trả lời kèm nguồn trích dẫn.")
        q = gr.Textbox(label="Câu hỏi", lines=2)
        btn = gr.Button("Hỏi", variant="primary")
        ans = gr.Markdown()
        src = gr.Markdown()
        gr.Examples(EXAMPLES, inputs=q)
        btn.click(ask, inputs=q, outputs=[ans, src])
        q.submit(ask, inputs=q, outputs=[ans, src])
    return ui


def launch_ui(bot, share=True):
    """Works for Gradio 4 and 5+. SSR (Gradio 5 default) is turned off: with it, share links on
    Kaggle/Colab often never return the answer."""
    ui = build_ui(bot)
    ui.queue()
    try:
        ui.launch(share=share, debug=True, ssr_mode=False)
    except TypeError:
        ui.launch(share=share, debug=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--retriever", default="bm25_legal", choices=list(CONFIGS))
    ap.add_argument("--llm", default=config.LLM_MODEL)
    ap.add_argument("--load-in-4bit", action="store_true")
    ap.add_argument("--cli", default=None)
    a = ap.parse_args()
    bot = Bot(a.retriever, a.llm, load_in_4bit=a.load_in_4bit)
    if a.cli:
        ans, src = bot.answer(a.cli)
        print("TRẢ LỜI:\n", ans, "\n\nNGUỒN:\n", src)
        return
    launch_ui(bot)


if __name__ == "__main__":
    main()
