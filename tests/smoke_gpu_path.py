"""Offline smoke test of the GPU code path (dense, rerank, LLM, cosine, demo) on CPU.

No model is downloaded: tiny randomly-initialised models (BERT embedder, BERT cross-encoder, Qwen2 causal LM)
and their tokenizers are created locally. The REAL scripts are then run end-to-end on a small corpus subset.
Answers are gibberish, of course; the goal is to catch crashes / wrong plumbing before spending GPU quota.

Needs: torch (CPU is fine), transformers, sentence-transformers, faiss-cpu.
Usage:  python -I tests/smoke_gpu_path.py [--keep]
"""
import json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
N_CHUNKS = 3000


def train_tokenizer(texts, kind):
    from tokenizers import Tokenizer, models, normalizers, pre_tokenizers, trainers, decoders
    if kind == "wordpiece":
        tok = Tokenizer(models.WordPiece(unk_token="[UNK]"))
        tok.normalizer = normalizers.NFC()
        tok.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
        tok.train_from_iterator(texts, trainers.WordPieceTrainer(vocab_size=3000, special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]))
    else:
        tok = Tokenizer(models.BPE())
        tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
        tok.decoder = decoders.ByteLevel()
        tok.train_from_iterator(texts, trainers.BpeTrainer(vocab_size=3000, special_tokens=["<|endoftext|>", "<|im_start|>", "<|im_end|>"],
                                                           initial_alphabet=pre_tokenizers.ByteLevel.alphabet()))
    return tok


def make_models(work, texts):
    import torch
    from transformers import (BertConfig, BertModel, BertForSequenceClassification, BertTokenizerFast,
                              PreTrainedTokenizerFast, Qwen2Config, Qwen2ForCausalLM)
    from sentence_transformers import SentenceTransformer, models as stm
    torch.manual_seed(0)
    # --- BERT tokenizer + embedder + reranker
    wp = train_tokenizer(texts, "wordpiece")
    btok = BertTokenizerFast(tokenizer_object=wp, unk_token="[UNK]", pad_token="[PAD]", cls_token="[CLS]",
                             sep_token="[SEP]", mask_token="[MASK]")
    bcfg = BertConfig(vocab_size=len(btok), hidden_size=32, num_hidden_layers=1, num_attention_heads=2,
                      intermediate_size=64, max_position_embeddings=512)
    raw = work / "tiny_bert"
    BertModel(bcfg).save_pretrained(raw); btok.save_pretrained(raw)
    t = stm.Transformer(str(raw), max_seq_length=128)
    emb_dir = work / "tiny-embedder"
    SentenceTransformer(modules=[t, stm.Pooling(t.get_word_embedding_dimension())]).save(str(emb_dir))
    rr_dir = work / "tiny-reranker"
    bcfg.num_labels = 1
    BertForSequenceClassification(bcfg).save_pretrained(rr_dir); btok.save_pretrained(rr_dir)
    # --- Qwen2-style causal LM with a chat template
    bpe = train_tokenizer(texts, "bpe")
    qtok = PreTrainedTokenizerFast(tokenizer_object=bpe, eos_token="<|im_end|>", pad_token="<|endoftext|>", bos_token=None)
    qtok.chat_template = ("{% for m in messages %}<|im_start|>{{ m['role'] }}\n{{ m['content'] }}<|im_end|>\n{% endfor %}"
                          "{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}")
    qcfg = Qwen2Config(vocab_size=len(qtok), hidden_size=64, intermediate_size=128, num_hidden_layers=2,
                       num_attention_heads=4, num_key_value_heads=2, max_position_embeddings=8192,
                       eos_token_id=qtok.eos_token_id, pad_token_id=qtok.pad_token_id, tie_word_embeddings=True)
    llm_dir = work / "tiny-llm"
    Qwen2ForCausalLM(qcfg).save_pretrained(llm_dir); qtok.save_pretrained(llm_dir)
    return emb_dir, rr_dir, llm_dir


def run(cmd, env):
    print("\n$", " ".join(str(c) for c in cmd), flush=True)
    r = subprocess.run([sys.executable, "-I", *map(str, cmd)], cwd=ROOT, env=env, capture_output=True, text=True)
    tail = (r.stdout + r.stderr).strip().splitlines()
    print("\n".join(l for l in tail[-12:] if "it/s]" not in l))
    if r.returncode != 0:
        print(r.stderr[-4000:])
        raise SystemExit(f"FAILED: {' '.join(map(str, cmd))}")


def main():
    work = Path(tempfile.mkdtemp(prefix="rag_smoke_"))
    art, res = work / "artifacts", work / "results"
    art.mkdir(); res.mkdir()
    real_art = ROOT / "artifacts"
    for name in ["legal", "baseline"]:
        src = real_art / f"chunks_{name}.jsonl"
        assert src.exists(), "run scripts/build_chunks.py first"
        with open(src, encoding="utf-8") as f, open(art / f"chunks_{name}.jsonl", "w", encoding="utf-8") as out:
            for i, line in enumerate(f):
                if i >= N_CHUNKS:
                    break
                out.write(line)
    texts = [json.loads(l)["text"] for l in open(art / "chunks_legal.jsonl", encoding="utf-8")]
    emb, rr, llm = make_models(work, texts)

    env = dict(os.environ, ARTIFACTS_DIR=str(art), RESULTS_DIR=str(res), REPORT_DIR=str(res), EMBEDDING_MODEL=str(emb),
               RERANKER_MODEL=str(rr), BASELINE_EMBEDDING=str(emb), BASELINE_LLM=str(llm), MAX_NEW_TOKENS="24",
               TOKENIZERS_PARALLELISM="false")
    run(["scripts/build_bm25.py", "--chunks", "legal"], env)
    run(["scripts/build_bm25.py", "--chunks", "baseline"], env)
    run(["scripts/build_dense.py", "--chunks", "baseline"], env)
    run(["scripts/build_dense.py", "--chunks", "legal"], env)
    run(["scripts/eval_retrieval.py", "--configs", "baseline", "dense_legal", "hybrid_legal", "hybrid_legal_rerank", "--k", "5"], env)
    lim = ["--limit", "3", "--max-new-tokens", "24"]
    run(["scripts/run_rag.py", "--name", "baseline", "--retriever", "baseline", "--llm", "baseline", "--fewshot", "none",
         "--batch-size", "1", "--limit", "3"], env)
    run(["scripts/run_rag.py", "--name", "baseline_noecho", "--retriever", "baseline", "--llm", "baseline-noecho",
         "--fewshot", "none", "--batch-size", "1", "--limit", "3"], env)
    run(["scripts/run_rag.py", "--name", "D_hybrid_rerank", "--retriever", "hybrid_legal_rerank", "--llm", llm, "--fewshot", "static", *lim], env)
    run(["scripts/run_rag.py", "--name", "F_qamem", "--retriever", "bm25_legal", "--llm", llm, "--fewshot", "similar", "--qa-memory", "2", *lim], env)
    run(["scripts/run_rag.py", "--name", "D_hybrid_rerank", "--retriever", "hybrid_legal_rerank", "--llm", llm, *lim], env)  # resume: 0 to run
    run(["scripts/evaluate.py"], env)
    run(["scripts/error_analysis.py", "--n", "1"], env)
    run(["scripts/make_tables.py"], env)
    run(["app/demo.py", "--retriever", "hybrid_legal_rerank", "--llm", llm, "--cli", "Mức lương cơ sở là bao nhiêu?"], env)

    p = __import__("pandas").read_csv(res / "predictions" / "baseline.csv")
    assert p.prediction.iloc[0].lstrip().startswith("Bạn là một trợ lý"), "faithful baseline must echo the prompt"
    p2 = __import__("pandas").read_csv(res / "predictions" / "baseline_noecho.csv")
    assert "Ngữ cảnh:" not in str(p2.prediction.iloc[0]), "noecho baseline must not contain the prompt"
    s = __import__("pandas").read_csv(res / "metrics" / "summary.csv")
    assert s.Cosine_Similarity.notna().all()
    print("\n✅ GPU code path smoke test passed. Workdir:", work)
    if "--keep" not in sys.argv:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
