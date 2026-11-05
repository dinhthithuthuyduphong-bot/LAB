"""Central configuration. Override any value with an environment variable of the same name."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _env(name, default):
    v = os.environ.get(name)
    if v is None:
        return default
    return type(default)(v) if not isinstance(default, Path) else Path(v)


# ---- Paths ----
CORPUS_DIR = _env("CORPUS_DIR", ROOT / "Dataset" / "export_1")
RES_XLSX = _env("RES_XLSX", ROOT / "doc" / "RES.xlsx")
DATA_DIR = _env("DATA_DIR", ROOT / "data")            # small, committed (res.csv, eval split)
ARTIFACTS_DIR = _env("ARTIFACTS_DIR", ROOT / "artifacts")  # large, git-ignored (chunks, indexes)
RESULTS_DIR = _env("RESULTS_DIR", ROOT / "results")

RES_CSV = DATA_DIR / "res.csv"
EVAL_CSV = DATA_DIR / "eval_set.csv"          # fixed evaluation subset (never used for few-shot)
FEWSHOT_CSV = DATA_DIR / "fewshot_pool.csv"   # QA pairs allowed for few-shot examples

# ---- Reproducibility ----
SEED = _env("SEED", 42)
EVAL_N = _env("EVAL_N", 200)   # assignment requires >= 100

# ---- Baseline settings (do not change: used as reference) ----
BASELINE_CHUNK_SIZE = 2000
BASELINE_CHUNK_OVERLAP = 50
BASELINE_EMBEDDING = "keepitreal/vietnamese-sbert"
BASELINE_LLM = "Qwen/Qwen1.5-1.8B"
BASELINE_TOP_K = 5

# ---- Improved pipeline settings ----
CHUNK_SIZE = _env("CHUNK_SIZE", 1000)        # characters
CHUNK_OVERLAP = _env("CHUNK_OVERLAP", 150)
EMBEDDING_MODEL = _env("EMBEDDING_MODEL", "bkai-foundation-models/vietnamese-bi-encoder")
RERANKER_MODEL = _env("RERANKER_MODEL", "BAAI/bge-reranker-v2-m3")
LLM_MODEL = _env("LLM_MODEL", "Qwen/Qwen2.5-3B-Instruct")
RETRIEVE_K = _env("RETRIEVE_K", 20)   # candidates before rerank
TOP_K = _env("TOP_K", 5)              # chunks given to the LLM
MAX_NEW_TOKENS = _env("MAX_NEW_TOKENS", 640)
MAX_CONTEXT_CHARS = _env("MAX_CONTEXT_CHARS", 6000)

# Cosine metric must always use the SAME embedding as the baseline for a fair comparison
METRIC_EMBEDDING = BASELINE_EMBEDDING
