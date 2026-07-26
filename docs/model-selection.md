# Model-selection results

Audit trail for the pinned model decision — every model tried across Weeks 6–7,
on the **same** stratified split (`random_state=42`, `test_size=0.2`), predicting
ESI (1–5). Metrics are macro-averaged so every acuity level counts equally.

> **Status: DRAFT.** Some cells are filled from the Week 7 decision journal and
> six-axis benchmark; cells still marked `_TBD_` are not quoted in those sources.
> Regenerate the full table in one command once the data file is in place:
> `python scripts/benchmark.py --config config.yaml` — that rewrites this file
> from the actual pipeline so the numbers can never drift from the code.

| Model | Key hyperparameters | Accuracy | Precision | Recall | F1 | Recall ESI-1 | Train (s) | Infer (ms) |
|---|---|---|---|---|---|---|---|---|
| Dummy (stratified) | strategy=stratified | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Logistic Regression | max_iter=1000, scaled | _TBD_ | _TBD_ | _TBD_ | _TBD_ | 0.250 | _TBD_ | _TBD_ |
| Decision Tree | max_depth=5 | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| **Random Forest ⭐** | n_estimators=300, class_weight=balanced | _TBD_ | _TBD_ | 0.553 | _TBD_ | 0.500 | _TBD_ | 0.057 |
| Random Forest (tuned) | RandomizedSearchCV, cv=3, f1_macro | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Gradient Boosting | max_depth=6, learning_rate=0.1, max_iter=300, class_weight=balanced | _TBD_ | _TBD_ | _TBD_ | _TBD_ | 0.125 | _TBD_ | _TBD_ |
| Small MLP | hidden_layer_sizes=(64,32), alpha=1e-3, scaled | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

⭐ = **winning / pinned model** (the Week 7 recommendation).

**Why Random Forest won:** it gave the best ESI-1 recall (0.500 — eight of sixteen
critical patients identified, versus four for logistic regression and two for gradient
boosting) and the best macro recall (0.553), while staying interpretable enough for
clinical governance (rated "Medium" on the one-minute test, vs "Low" for gradient
boosting) and keeping inference negligible at 0.057 ms per prediction. Logistic
regression is retained as the documented fallback. Gradient boosting scored higher on
overall accuracy, but that is irrelevant when it misses fourteen of sixteen ESI-1
patients. Full reasoning: `Week-7/Decision Journal_ Week 7 Model Choice.pdf`.

**Caveat (from the journal):** the ESI-1 advantage rests on only sixteen test patients
— a margin of four correct classifications — and needs re-estimating on a larger sample.

### How to read this table
- **Accuracy** — overall fraction correct. Misleading alone because ESI 3 dominates.
- **Precision / Recall / F1 (macro)** — averaged equally across all five ESI levels.
- **Recall ESI-1** — the number the triage use-case cares about most: the fraction of
  the *sickest* patients the model correctly flags as ESI 1.
- **Train (s) / Infer (ms)** — cost of retraining and of scoring the test set.