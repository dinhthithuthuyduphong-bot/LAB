"""Question box that runs inside a Jupyter / Kaggle / Colab notebook (no public link, no network tunnel).

    from notebook_ui import notebook_ui, hoi
    notebook_ui(bot)                 # text box + button, answers appear under the cell
    hoi(bot, "Câu hỏi ...")          # fallback without widgets: one call = one answer
"""
import traceback

from IPython.display import Markdown, clear_output, display


def _render(q, ans, src):
    display(Markdown(f"### ❓ {q}\n\n{ans}\n\n---\n**Nguồn:**\n\n{src}"))


def hoi(bot, q):
    ans, src = bot.answer(q)
    _render(q, ans, src)


def notebook_ui(bot):
    import ipywidgets as w
    box = w.Textarea(placeholder="Nhập câu hỏi pháp luật…", layout=w.Layout(width="100%", height="80px"))
    btn = w.Button(description="Hỏi", button_style="primary")
    out = w.Output()

    def on_click(_):
        q = box.value.strip()
        with out:
            clear_output()
            if not q:
                print("Hãy nhập câu hỏi.")
                return
            print("Đang trả lời (khoảng 10–20 giây)…")
            try:
                ans, src = bot.answer(q)
                clear_output()
                _render(q, ans, src)
            except Exception:
                clear_output()
                print(traceback.format_exc())

    btn.on_click(on_click)
    display(w.VBox([box, btn, out]))
