"""Pick few-shot examples / QA-memory entries from data/fewshot_pool.csv (never from the eval set). CPU only."""
import pandas as pd

from . import config
from .metrics import jaccard_similarity
from .retrieval import BM25Retriever


class ExamplePool:
    def __init__(self, path=config.FEWSHOT_CSV, exclude_ids=()):
        df = pd.read_csv(path)
        ev_ids = set(pd.read_csv(config.EVAL_CSV).id) if config.EVAL_CSV.exists() else set()
        df = df[~df.id.isin(ev_ids | set(exclude_ids))].reset_index(drop=True)
        self.df = df
        self.bm25 = BM25Retriever(bigrams=True).fit(df.question.tolist(), show_progress=False)

    def static(self, n=1, max_answer_chars=1200):
        """Fixed, short, well-formed examples (answer starts with 'Căn cứ') — same for every question."""
        d = self.df[self.df.answer.str.startswith("Căn cứ") & (self.df.answer.str.len() < max_answer_chars)]
        return d.sample(n, random_state=config.SEED)[["question", "answer"]].to_dict("records")

    def similar(self, question, n=1, max_question_jaccard=0.8):
        """Most similar pool questions (BM25). Near-duplicates (jaccard > threshold) are skipped to
        avoid answering an eval question with its own paraphrase."""
        out = []
        for i, _ in self.bm25.search(question, k=n + 10):
            row = self.df.iloc[i]
            if jaccard_similarity(question, row.question) > max_question_jaccard:
                continue
            out.append({"question": row.question, "answer": row.answer})
            if len(out) == n:
                break
        return out
