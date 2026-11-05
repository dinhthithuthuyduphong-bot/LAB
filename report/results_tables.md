# Bảng kết quả (sinh tự động bởi `scripts/make_tables.py`)

## Kết quả chính (tất cả câu trong eval set)

| name                        |   n |   Cosine_Similarity |   Jaccard_Similarity |   Token_Overlap |   BLEU_Score |   ROUGE_L |   avg_pred_words |
|:----------------------------|----:|--------------------:|---------------------:|----------------:|-------------:|----------:|-----------------:|
| extractive_bm25_baseline_k5 | 200 |                 nan |               0.2506 |          0.3974 |       0.2821 |    0.1791 |         418.3000 |
| extractive_bm25_legal_k5    | 200 |                 nan |               0.2798 |          0.4313 |       0.3060 |    0.2040 |         398.6000 |

## Nhóm `covered`

| name                        |   n |   Cosine_Similarity |   Jaccard_Similarity |   Token_Overlap |   BLEU_Score |   ROUGE_L |   avg_pred_words |
|:----------------------------|----:|--------------------:|---------------------:|----------------:|-------------:|----------:|-----------------:|
| extractive_bm25_baseline_k5 |  51 |                 nan |               0.3331 |          0.5223 |       0.3861 |    0.2833 |         418.6000 |
| extractive_bm25_legal_k5    |  51 |                 nan |               0.4049 |          0.5548 |       0.4146 |    0.3366 |         393.9000 |

## Nhóm `not_covered`

| name                        |   n |   Cosine_Similarity |   Jaccard_Similarity |   Token_Overlap |   BLEU_Score |   ROUGE_L |   avg_pred_words |
|:----------------------------|----:|--------------------:|---------------------:|----------------:|-------------:|----------:|-----------------:|
| extractive_bm25_baseline_k5 | 149 |                 nan |               0.2223 |          0.3546 |       0.2465 |    0.1435 |         418.2000 |
| extractive_bm25_legal_k5    | 149 |                 nan |               0.2370 |          0.3890 |       0.2689 |    0.1586 |         400.2000 |

## Retrieval (không LLM)

| config             |   k |   DocRecall@1(covered) |   DocRecall@k(covered) |   MRR(covered) |   CtxTokenRecall(all) |   CtxTokenRecall(covered) |   CtxTokenRecall(not_covered) |   avg_ctx_chars |
|:-------------------|----:|-----------------------:|-----------------------:|---------------:|----------------------:|--------------------------:|------------------------------:|----------------:|
| bm25_baseline      |   1 |                 0.4706 |                 0.4706 |         0.4706 |                0.4719 |                    0.5529 |                        0.4442 |       1945.3550 |
| bm25_legal         |   1 |                 0.4706 |                 0.4706 |         0.4706 |                0.3503 |                    0.4444 |                        0.3181 |        810.5750 |
| bm25_legal_noboost |   1 |                 0.4706 |                 0.4706 |         0.4706 |                0.3503 |                    0.4444 |                        0.3181 |        810.5750 |
| bm25_baseline      |   5 |                 0.4706 |                 0.7843 |         0.6059 |                0.7533 |                    0.7920 |                        0.7400 |       9739.1200 |
| bm25_legal         |   5 |                 0.4706 |                 0.7843 |         0.6062 |                0.6334 |                    0.6994 |                        0.6108 |       4059.1050 |
| bm25_legal_noboost |   5 |                 0.4706 |                 0.7843 |         0.6062 |                0.6335 |                    0.6997 |                        0.6108 |       4061.4400 |
| bm25_baseline      |  10 |                 0.4706 |                 0.8235 |         0.6116 |                0.8344 |                    0.8583 |                        0.8262 |      19525.9450 |
| bm25_legal         |  10 |                 0.4706 |                 0.8235 |         0.6111 |                0.7317 |                    0.7708 |                        0.7184 |       7910.4600 |
| bm25_legal_noboost |  10 |                 0.4706 |                 0.8235 |         0.6111 |                0.7318 |                    0.7711 |                        0.7184 |       7912.7950 |

## Cấu hình và chi phí chạy

| name                        | retriever     | llm        | fewshot   |   qa_memory |   n |   sec_per_q | max_gpu_gb   |
|:----------------------------|:--------------|:-----------|:----------|------------:|----:|------------:|:-------------|
| extractive_bm25_baseline_k5 | bm25_baseline | extractive | none      |           0 | 200 |        0    |              |
| extractive_bm25_legal_k5    | bm25_legal    | extractive | none      |           0 | 200 |        0.01 |              |
