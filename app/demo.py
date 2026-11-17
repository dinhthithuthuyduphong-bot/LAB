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

EXAMPLES = [   # checked: BM25 retrieves the right document for each of these
    "Mức lương cơ sở từ ngày 01/7/2024 là bao nhiêu?",
    "Chế độ tiền thưởng theo Nghị định 73/2024/NĐ-CP được thực hiện như thế nào?",
    "Chế độ nghỉ hằng năm của người lao động được quy định như thế nào?",
    "Người lao động nghỉ việc được trợ cấp thôi việc như thế nào?",
    "Dịp lễ 30/4 và 1/5 năm 2025 công chức được nghỉ mấy ngày, có phải làm bù không?",
    "Ngạch thủ kho, thủ quỹ ngân hàng có chức trách gì theo Thông tư 14/2022/TT-NHNN?",
]


class Bot:
    def __init__(self, retriever="bm25_legal", llm=config.LLM_MODEL, top_k=config.TOP_K, load_in_4bit=False):
        self.retr = Retriever(CONFIGS[retriever])
        self.top_k = top_k
        self.llm = None
        if llm != "extractive":
            from src.llm import HFChatLLM
            self.llm = HFChatLLM(llm, max_new_tokens=config.MAX_NEW_TOKENS, load_in_4bit=load_in_4bit)
            print(f"LLM {llm} loaded on: {self.llm.model.device}"
                  + ("" if "cuda" in str(self.llm.model.device) else "  ⚠️ CPU: answers will be very slow, enable a GPU"))
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
