"""Sanity tests for the CPU components.  Run:  python -I tests/test_core.py"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.metrics import normalize_text, rouge_l_score, bleu_score_simple, jaccard_similarity, token_overlap_score
from src.legal_text import clean_text, find_doc_ids, normalize_doc_id, doc_id_from_filename, split_info_block
from src.chunking import legal_chunks, baseline_chunks
from src.postprocess import clean_answer
from src.retrieval import rrf


def rouge_l_reference(pred, true):
    """Exact copy of the baseline notebook implementation (full DP table)."""
    pw, tw = normalize_text(pred).split(), normalize_text(true).split()
    if not pw or not tw:
        return 0.0
    m, n = len(pw), len(tw)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if pw[i - 1] == tw[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[m][n]
    p, r = lcs / m, lcs / n
    return 2 * p * r / (p + r) if p + r else 0.0


def test_metrics():
    rnd = random.Random(0)
    vocab = "căn cứ điều khoản lương cơ sở người lao động được nghỉ ngày tết".split()
    for _ in range(300):
        a = " ".join(rnd.choice(vocab) for _ in range(rnd.randint(0, 30)))
        b = " ".join(rnd.choice(vocab) for _ in range(rnd.randint(1, 30)))
        assert abs(rouge_l_score(a, b) - rouge_l_reference(a, b)) < 1e-12
    assert jaccard_similarity("a b", "a b") == 1.0
    assert token_overlap_score("Lương cơ sở.", "lương cơ sở") == 1.0
    assert bleu_score_simple("", "x") == 0.0


def test_text():
    assert find_doc_ids("Theo Thông tư 50/2024/TT-NHNN và Nghị định 52/2024/NĐ-CP") == ["50/2024/TT-NHNN", "52/2024/NĐ-CP"]
    assert doc_id_from_filename("01_2005_QĐ-UB_1.txt") == "01/2005/QĐ-UB"
    assert normalize_doc_id("04/CTr-UBND") == "04/CTR-UBND"
    raw = "CỘNG HÒA\n XÃ HỘI\n\nĐiều 1.\nNội dung\n dài\n\n--- THÔNG TIN THÊM ---\nSo hieu: 1/QĐ-UB\nLinh vuc nganh: Lao động - Tiền lương\n\n--- MỤC LỤC ---\n- x"
    body, info = split_info_block(raw)
    assert info["info_doc_id"] == "1/QĐ-UB" and "MỤC LỤC" not in body
    assert clean_text(raw) == "CỘNG HÒA XÃ HỘI\nĐiều 1. Nội dung dài"


def test_chunking():
    text = "\n".join([f"Điều {i}. Tiêu đề {i}\n" + ("Nội dung quy định rất dài. " * 60) for i in range(1, 4)])
    ch = legal_chunks(text, {"doc_type": "Nghị định", "doc_id": "1/2024/NĐ-CP", "title": "NGHỊ ĐỊNH X"}, size=500, overlap=100)
    assert all(len(c["text"]) <= 600 for c in ch)
    assert all(c["dieu"].startswith("Điều") for c in ch)
    assert ch[0]["header"].startswith("[Nghị định 1/2024/NĐ-CP]")
    b = baseline_chunks("A" * 4500, 2000, 50)
    assert [len(x) for x in b] == [2000, 2000, 600]


def test_post_and_fusion():
    assert clean_answer("Căn cứ Điều 1.<|im_end|>\nCâu hỏi: tiếp") == "Căn cứ Điều 1."
    rep = "Đây là một câu khá dài được lặp lại nhiều lần trong output. " * 3
    assert clean_answer(rep).count("lặp lại") == 1
    assert rrf([[(1, 9), (2, 8)], [(2, 5), (3, 4)]])[0][0] == 2


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
