"""Evaluation metrics — identical to the formulas used in doc/Baseline.ipynb so numbers are comparable.

Cosine similarity needs an embedding function; pass `embed_fn(list[str]) -> np.ndarray`.
The assignment compares against the baseline, so use the baseline embedding
(keepitreal/vietnamese-sbert) for the cosine metric no matter which retriever you use.
"""
import re
from collections import Counter

import numpy as np

METRIC_NAMES = ["Cosine_Similarity", "Jaccard_Similarity", "Token_Overlap", "BLEU_Score", "ROUGE_L"]


def normalize_text(text: str) -> str:
    text = str(text).lower().replace("\n", " ").strip()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def jaccard_similarity(pred: str, true: str) -> float:
    p, t = set(normalize_text(pred).split()), set(normalize_text(true).split())
    return len(p & t) / len(p | t) if p and t else 0.0


def token_overlap_score(pred: str, true: str) -> float:
    p, t = normalize_text(pred).split(), normalize_text(true).split()
    if not t:
        return 0.0
    return sum((Counter(p) & Counter(t)).values()) / len(t)


def bleu_score_simple(pred: str, true: str) -> float:
    p, t = normalize_text(pred).split(), normalize_text(true).split()
    if not p or not t:
        return 0.0
    overlap = sum((Counter(p) & Counter(t)).values())
    precision = overlap / len(p)
    bp = 1.0 if len(p) >= len(t) else np.exp(1 - len(t) / len(p))
    return float(bp * precision)


def _lcs(a, b) -> int:
    # O(n*m) time, O(m) memory (same result as the baseline's full DP table)
    if len(a) < len(b):
        a, b = b, a
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b, 1):
            cur.append(prev[j - 1] + 1 if x == y else max(prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]


def rouge_l_score(pred: str, true: str) -> float:
    p, t = normalize_text(pred).split(), normalize_text(true).split()
    if not p or not t:
        return 0.0
    lcs = _lcs(p, t)
    prec, rec = lcs / len(p), lcs / len(t)
    return 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0


def lexical_metrics(pred: str, true: str) -> dict:
    return {
        "Jaccard_Similarity": jaccard_similarity(pred, true),
        "Token_Overlap": token_overlap_score(pred, true),
        "BLEU_Score": bleu_score_simple(pred, true),
        "ROUGE_L": rouge_l_score(pred, true),
    }


def cosine_scores(preds, trues, embed_fn) -> np.ndarray:
    """Row-wise cosine between pred and true embeddings. Empty strings score 0, as in the baseline."""
    preds, trues = [str(x) if x is not None else "" for x in preds], [str(x) for x in trues]
    out = np.zeros(len(preds))
    idx = [i for i, (p, t) in enumerate(zip(preds, trues)) if p.strip() and t.strip()]
    if not idx:
        return out
    a = np.asarray(embed_fn([preds[i] for i in idx]), dtype=np.float32)
    b = np.asarray(embed_fn([trues[i] for i in idx]), dtype=np.float32)
    a /= np.linalg.norm(a, axis=1, keepdims=True) + 1e-12
    b /= np.linalg.norm(b, axis=1, keepdims=True) + 1e-12
    out[idx] = (a * b).sum(1)
    return out
