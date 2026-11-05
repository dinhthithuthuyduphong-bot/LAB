"""Run a RAG configuration on the fixed eval set and cache the answers to results/predictions/<name>.csv.

Resumable: questions already present in the output file are skipped (useful when a Kaggle/Colab session
dies). Metrics are computed separately by scripts/evaluate.py, so changing a metric never needs the GPU again.

Usage (GPU):
  python -I scripts/run_rag.py --name ours_bm25 --retriever bm25_legal --llm Qwen/Qwen2.5-3B-Instruct
  python -I scripts/run_rag.py --name ours_hybrid_rerank --retriever hybrid_legal_rerank --fewshot static
Usage (CPU, no LLM — checks the whole pipeline and gives a lower-bound reference):
  python -I scripts/run_rag.py --name extractive_bm25 --retriever bm25_legal --llm extractive
  python -I scripts/run_rag.py --name dryrun --retriever bm25_legal --llm dry-run --limit 3
"""
import sys, argparse, json, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from tqdm import tqdm

from src import config
from src.postprocess import clean_answer
from src.prompts import build_messages, baseline_prompt, messages_to_text

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eval_retrieval import CONFIGS  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--retriever", default="bm25_legal", choices=list(CONFIGS))
    ap.add_argument("--llm", default=config.LLM_MODEL,
                    help="HF model id | 'baseline' (Qwen1.5-1.8B + baseline prompt, prompt echoed like the notebook) | "
                         "'baseline-noecho' (same, generated text only) | 'extractive' | 'dry-run'")
    ap.add_argument("--top-k", type=int, default=config.TOP_K)
    ap.add_argument("--max-context-chars", type=int, default=config.MAX_CONTEXT_CHARS)
    ap.add_argument("--max-new-tokens", type=int, default=config.MAX_NEW_TOKENS)
    ap.add_argument("--fewshot", choices=["none", "static", "similar"], default="static")
    ap.add_argument("--qa-memory", type=int, default=0, help="ablation: add N similar QA pairs from the pool as references")
    ap.add_argument("--batch-size", type=int, default=4)
    ap.add_argument("--load-in-4bit", action="store_true")
    ap.add_argument("--limit", type=int, default=None, help="debug on the first N questions")
    a = ap.parse_args()

    ev = pd.read_csv(config.EVAL_CSV)
    if a.limit:
        ev = ev.head(a.limit)
    out_dir = config.RESULTS_DIR / "predictions"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{a.name}.csv"
    done = set(pd.read_csv(out_path).id) if out_path.exists() and a.llm != "dry-run" else set()
    todo = ev[~ev.id.isin(done)]
    print(f"{len(done)} cached, {len(todo)} to run -> {out_path}")
    if todo.empty:
        return

    from src.retriever import Retriever
    retr = Retriever(CONFIGS[a.retriever])

    pool = None
    if a.fewshot != "none" or a.qa_memory:
        from src.fewshot import ExamplePool
        pool = ExamplePool()
    static_ex = pool.static(1) if a.fewshot == "static" else []

    llm = None
    is_baseline = a.llm in ("baseline", "baseline-noecho")
    if is_baseline:
        from src.llm import HFBaseLLM
        llm = HFBaseLLM(config.BASELINE_LLM, echo_prompt=(a.llm == "baseline"))
    elif a.llm not in ("extractive", "dry-run"):
        from src.llm import HFChatLLM
        llm = HFChatLLM(a.llm, max_new_tokens=a.max_new_tokens, load_in_4bit=a.load_in_4bit)

    meta = vars(a).copy()
    (out_dir / f"{a.name}.config.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))

    rows = todo.to_dict("records")
    for s in tqdm(range(0, len(rows), a.batch_size), desc=a.name, mininterval=10):
        batch = rows[s:s + a.batch_size]
        t0 = time.time()
        items = []
        for q in batch:
            hits = retr.retrieve(q["question"], top_k=a.top_k)
            ex = static_ex if a.fewshot == "static" else (pool.similar(q["question"], 1) if a.fewshot == "similar" else [])
            mem = pool.similar(q["question"], a.qa_memory) if a.qa_memory else []
            if is_baseline:
                prompt = baseline_prompt(q["question"], hits)
            else:
                prompt = build_messages(q["question"], hits, examples=ex, max_context_chars=a.max_context_chars, qa_memory=mem)
            items.append((q, hits, prompt))

        if a.llm == "extractive":
            raw = ["\n".join(h["text"] for h in hits)[:a.max_context_chars] for _, hits, _ in items]
        elif a.llm == "dry-run":
            for q, hits, p in items:
                print("=" * 80, "\n", p if isinstance(p, str) else messages_to_text(p))
            continue
        else:
            raw, _ = llm.generate([p for _, _, p in items])
        dt = (time.time() - t0) / len(batch)

        recs = []
        for (q, hits, p), r in zip(items, raw):
            recs.append({"id": q["id"], "group": q["group"], "question": q["question"],
                         "prediction": r if a.llm == "baseline" else clean_answer(r), "raw_output": r,
                         "retrieved": "|".join(f"{h['doc_id']}#{h['chunk_id']}" for h in hits),
                         "sec_per_q": round(dt, 2)})
        pd.DataFrame(recs).to_csv(out_path, mode="a", header=not out_path.exists(), index=False)


if __name__ == "__main__":
    main()
