# Model-selection results

Audit trail for the pinned model decision — every model tried across Weeks 6–7,
evaluated on the **same** stratified split (`random_state=42`, `test_size=0.2`) of the
full dataset, predicting ESI (1–5). Precision, recall, and F1 are macro-averaged so
every acuity level counts equally.

| Model | Key hyperparameters | Accuracy | Precision | Recall | F1 | Recall ESI-1 | Train (s) | Infer (ms) |
|---|---|---|---|---|---|---|---|---|
| Dummy (stratified) | strategy=stratified | 0.375 | 0.204 | 0.204 | 0.204 | 0.000 | 0.00 | 19.6 |
| Logistic Regression | max_iter=1000, scaled | 0.671 | 0.572 | 0.452 | 0.481 | 0.188 | 3.06 | 35.9 |
| Decision Tree | max_depth=5 | 0.556 | 0.265 | 0.245 | 0.216 | 0.000 | 0.28 | 27.4 |
| **Random Forest ⭐** | n_estimators=300, class_weight=balanced | 0.641 | 0.470 | 0.369 | 0.390 | 0.000 | 45.49 | 1548.0 |
| Gradient Boosting | max_depth=6, learning_rate=0.1, max_iter=300, class_weight=balanced | 0.550 | 0.410 | 0.547 | 0.416 | 0.313 | 8.03 | 127.8 |
| Small MLP | hidden_layer_sizes=(64,32), alpha=1e-3, scaled | 0.638 | 0.526 | 0.482 | 0.499 | 0.313 | 104.92 | 67.2 |

⭐ = **chosen model** — the Week 7 recommendation. Full reasoning:
`Week-7/Decision Journal_ Week 7 Model Choice.pdf`.

## Decision note

The Random Forest was selected in Week 7 as the Phase 3 triage model, with logistic
regression retained as the documented fallback (see the linked decision journal). That
choice was made on a small test sample, where the Random Forest led on ESI-1 recall.

The table above re-evaluates every model on the **full dataset**, as the Week 7 journal's
"things I do not yet know" section explicitly recommended. On the larger sample the
ESI-1 result shifts: Gradient Boosting leads on both macro recall (0.547) and ESI-1
recall (0.313), while the Random Forest's ESI-1 recall falls to 0.000. This reversal is
flagged for review at the start of Phase 3 before the model is confirmed for deployment,
consistent with the caveat recorded in the original journal.

## How to read this table

- **Accuracy** — overall fraction correct; misleading alone because ESI 3 dominates.
- **Precision / Recall / F1 (macro)** — averaged equally across all five ESI levels.
- **Recall ESI-1** — the fraction of the sickest patients correctly flagged as ESI 1; the
  metric the triage use-case weighs most heavily.
- **Train (s) / Infer (ms)** — cost of retraining and of scoring the test set.