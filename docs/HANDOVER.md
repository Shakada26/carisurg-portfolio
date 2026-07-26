# Handover — CariSurg ED triage-acuity model

_Audience: a new hire cloning this repo on a Monday morning, and Dr. De Fretias
auditing the decision. If you can read this page and run the model by end of day,
it has done its job._

## 1 · Project summary
This project trains and hands over a machine-learning model that predicts a
patient's Emergency Severity Index (ESI, 1-5) from information captured at
triage — vital signs and chief-complaint flags. It is decision-support for ED
triage, not an autonomous system: it surfaces an acuity estimate for a clinician
to confirm or override. The repo covers the full path from the raw triage export
to a single pinned, reproducible model.

## 2 · Final model decision
- Winner: Random Forest (RandomForestClassifier, n_estimators=300,
  class_weight="balanced"), with logistic regression retained as the documented fallback.
- One-sentence reason: it gave the best ESI-1 recall (0.500) and the best macro recall
  while staying interpretable enough for clinical governance — gradient boosting scored
  higher on accuracy but missed far more critical ESI-1 patients.

## 3 · How to run
    git clone <repo-url> && cd carisurg-portfolio
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    # put the data file at data/yaleemmlc_admissionprediction_triage.csv (see section 4)
    python scripts/train.py --config config.yaml       # train + evaluate the pinned model
    python scripts/benchmark.py --config config.yaml   # (optional) rebuild the results table
    pytest -q                                          # run the sanity checks

All settings — paths, seed, model, hyperparameters — live in config.yaml. Change
behaviour there, not in the code.

## 4 · Where the data lives & governance status
- File: yaleemmlc_admissionprediction_triage.csv, expected in data/ (path set in
  config.yaml). The CSV is NOT committed to the repo.
- Source: the triage extract provided to the CariSurg project (Yale EM
  admission-prediction dataset).
- Governance: fill in the current status — data-use agreement / ethics approval
  reference, who owns access, whether the extract is de-identified, and where the
  master copy is stored. Fairness-sensitive fields (race, ethnicity, language,
  religion, insurance) are excluded from the baseline feature set by default
  (drop_demographics: true).

## 5 · Known limitations
- Single split, single seed. Metrics come from one 80/20 stratified split
  (random_state=42); they are not cross-validated confidence intervals.
- Class imbalance on rare classes. ESI 1 and ESI 5 are uncommon, so recall on the
  sickest patients (ESI-1) is the metric to watch and is sensitive to the
  imputation and class_weight choices.
- Median imputation + retrospective data. Missing vitals are median-filled and the
  model is trained on historical records; performance on live data, other sites,
  or shifted case-mix is unverified and needs prospective validation before any
  clinical use.