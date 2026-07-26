# Model-selection results

Audit trail for the pinned model decision — every model tried across Weeks 6–7,
on the **same** stratified split (`random_state=42`, `test_size=0.2`), predicting
ESI (1–5). Metrics are macro-averaged so every acuity level counts equally.

> **Status: DRAFT.** The metric cells below are placeholders. Regenerate the
> real numbers in one command once the data file is in place:
> `python scripts/benchmark.py --config config.yaml`
> That rewrites this file from the actual pipeline, so the numbers can never
> drift from the code. Placeholders are shown as `_TBD_`.

| Model | Key hyperparameters | Accuracy | Precision | Recall | F1 | Recall ESI-1 | Train (s) | Infer (ms) |
|---|---|---|---|---|---|---|---|---|
| Dummy (stratified) | strategy=stratified | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Logistic Regression | max_iter=1000, scaled | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Decision Tree | max_depth=5 | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Random Forest | n_estimators=300, class_weight=balanced | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Random Forest (tuned) | RandomizedSearchCV, cv=3, f1_macro | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| **Gradient Boosting ⭐** | max_depth=6, learning_rate=0.1, max_iter=300, class_weight=balanced | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Small MLP | hidden_layer_sizes=(64,32), alpha=1e-3, scaled | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

⭐ = **winning / pinned model** (the Week 7 recommendation).

**Why Gradient Boosting won:** _one-line summary here — see the full reasoning in
the Week 7 decision journal in `notebooks/`._ Typical rationale to adapt to your
numbers: it gave the best macro-F1 and the strongest recall on the critical
ESI-1 class without the training cost of the tuned forest, and needs no scaling.

### How to read this table
- **Accuracy** — overall fraction correct. Misleading alone because ESI 3 dominates.
- **Precision / Recall / F1 (macro)** — averaged equally across all five ESI levels.
- **Recall ESI-1** — the number the triage use-case cares about most: the fraction
  of the *sickest* patients the model correctly flags as ESI 1.
- **Train (s) / Infer (ms)** — cost of retraining and of scoring the test set.