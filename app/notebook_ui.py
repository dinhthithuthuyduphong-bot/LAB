"""Question box that runs inside a Jupyter / Kaggle / Colab notebook (no public link, no network tunnel).

    from notebook_ui import notebook_ui, hoi
    notebook_ui(bot)                 # text box + button, answers appear under the cell
    hoi(bot, "Câu hỏi ...")          # fallback without widgets: one call = one answer
"""
import threading
import time
import traceback

from IPython.display import Markdown, clear_output, display


def _render(q, ans, src):
    display(Markdown(f"### ❓ {q}\n\n{ans}\n\n---\n**Nguồn:**\n\n{src}"))


def hoi(bot, q):
    warn = device_warning(bot)
    if warn:
        print(warn)
    t0 = time.time()
    ans, src = bot.answer(q)
    _render(q, ans, src)
    print(f"({time.time() - t0:.0f} giây)")


def device_warning(bot):
    """Return a warning string when the LLM is not on a GPU (answers would take many minutes)."""
    llm = getattr(bot, "llm", None)
    if llm is None:
        return ""
    dev = str(getattr(llm.model, "device", ""))
    if "cuda" not in dev:
        return ("⚠️ LLM đang chạy trên CPU, mỗi câu có thể mất trên 10 phút. Hãy bật GPU (Session options → "
                "Accelerator → GPU T4) rồi chạy lại notebook.")
    return ""


def notebook_ui(bot, max_new_tokens=400):
    """max_new_tokens: shorter answers for a responsive demo (evaluation used 640)."""
    if getattr(bot, "llm", None) is not None and max_new_tokens:
        bot.llm.max_new_tokens = max_new_tokens
    warn = device_warning(bot)
    if warn:
        print(warn)
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
            status = w.Label("Đang trả lời… 0 giây (thường 20–60 giây trên GPU)")
            display(status)
            t0, done = time.time(), threading.Event()

            def tick():                       # live elapsed-time counter while the model generates
                while not done.wait(1):
                    status.value = f"Đang trả lời… {time.time() - t0:.0f} giây (thường 20–60 giây trên GPU)"
            threading.Thread(target=tick, daemon=True).start()
            try:
                ans, src = bot.answer(q)
                done.set()
                clear_output()
                _render(q, ans, src)
                print(f"({time.time() - t0:.0f} giây)")
            except Exception:
                done.set()
                clear_output()
                print(traceback.format_exc())

    def on_click_safe(b):
        btn.disabled = True                   # avoid queuing several questions by double-clicking
        try:
            on_click(b)
        finally:
            btn.disabled = False

    btn.on_click(on_click_safe)
    display(w.VBox([box, btn, out]))
