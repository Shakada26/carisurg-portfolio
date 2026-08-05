# Model Card — the engine behind the Week 9 design

This card ties the Week 9 prototype and mock-ups to the model built in Weeks 5 to 8, so the design is grounded in real work. The source code lives in the project repository (src, scripts, config.yaml) and the Week 5 to 7 notebooks.

## What the model does
Given a patient's triage data at the front door, the model predicts the **ESI triage level (1 to 5)**. A simple view groups **ESI 1 and 2 as urgent** and ESI 3 to 5 as not urgent.

## Data
- **Source:** the Yale EMMLC admission prediction triage extract, a de identified set of emergency department arrivals.
- **Target:** `esi`.
- **Split:** one stratified 80 / 20 split, `random_state=42`, used for every model so the comparison is fair.

## Features the model is allowed to see
- **Triage vitals:** `triage_vital_hr`, `triage_vital_sbp`, `triage_vital_dbp`, `triage_vital_rr`, `triage_vital_o2`, `triage_vital_temp`, `triage_glucose`.
- **Chief complaint flags:** the binary body system flags for the patient's stated reason for coming in.
- **Engineered flags (Week 7):** thresholds such as `is_bradycardic` (heart rate below 60).

## Deliberately excluded (design and ethics decisions)
- **Demographics** (age, gender, ethnicity, race, language, religion, marital status, employment, insurance) are held out to reduce unfair bias.
- **Outcome columns** (`disposition`, `previousdispo`) are removed as leakage, because they are known only after triage.
- **Administrative and arrival fields** are excluded as not clinically informative.

## Models compared
Dummy baseline, Logistic Regression (scaled, `max_iter=1000`), Decision Tree (`max_depth=5`), Random Forest (`n_estimators=300, class_weight=balanced`), Gradient Boosting (`max_depth=6, learning_rate=0.1, max_iter=300, class_weight=balanced`), and a small MLP.

## How it is judged
Accuracy alone is misleading because ESI 3 dominates. Precision, recall and F1 are macro averaged so every level counts. **The headline safety metric is recall for ESI 1**, the fraction of the sickest patients caught, because under triage of a critical patient is the worst error.

## Results (full dataset)

| Model | Accuracy | Macro F1 | Macro recall | Recall ESI 1 |
|---|---|---|---|---|
| Dummy (stratified) | 0.375 | 0.204 | 0.204 | 0.000 |
| Logistic Regression | 0.671 | 0.481 | 0.452 | 0.188 |
| Decision Tree | 0.556 | 0.216 | 0.245 | 0.000 |
| Random Forest | 0.641 | 0.390 | 0.369 | 0.000 |
| Gradient Boosting | 0.550 | 0.416 | 0.547 | 0.313 |
| Small MLP | 0.638 | 0.499 | 0.482 | 0.313 |

## The decision, told honestly
In Week 7 I chose **Random Forest** on a small test sample, where it led on ESI 1 recall, with Logistic Regression kept as the fallback. My Week 7 journal said the next step was to re test on the full dataset.

When I did that, the result reversed. On the full data **Gradient Boosting** leads on both macro recall (0.547) and ESI 1 recall (0.313), while **Random Forest falls to 0.000** on ESI 1, catching none of the sickest patients. The model choice is therefore **flagged for review at the start of Phase 3** before anything is confirmed. I will not confirm a model that misses every critical patient.

**Honest limitation:** even the best model catches only about 31 percent of ESI 1 cases. This is a proof of concept, not a deployable model. The next step is lifting ESI 1 recall specifically, through class rebalancing, threshold tuning, cost sensitive learning, and more critical case data.

## How the Week 9 design uses this
- The prototype queue is ordered by predicted acuity, and each patient shows plain English drivers from these vitals.
- The **safety hold** (no score on missing vitals) mirrors the missing data handling in the model.
- The **Friction Protocol** (nurse scores first, then the model reveals) exists precisely because recall for ESI 1 is still low. The model is there to support the nurse, never to replace them.

## Source code
- Repository: `src/` (data, features, model, utils), `scripts/train.py`, `scripts/benchmark.py`, `config.yaml`.
- Notebooks: Week 5 (data literacy, profiling), Week 6 (logistic regression, decision tree, evaluation), Week 7 (optimisation).
