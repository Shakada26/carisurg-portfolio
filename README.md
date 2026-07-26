# CariSurg MedTech Pathways Programme Portfolio

**Student:** Shakada Blake
**Programme:** CariSurg MedTech Pathways, Cohort 2026
**Start:** May 2026

A structured learning portfolio in clinical AI, emergency-department (ED) triage
analytics, healthcare data science, and reproducible research with Git and GitHub.

---

## 1. Project Overview

This repository documents a 12-week applied research project: the design and
evaluation of a **non-autonomous, human-in-the-loop AI decision-support tool** for
standardising ED triage intake at Mercer General Hospital, with a focus on staying
reliable when biometric data is missing.

The tool predicts a patient's **Emergency Severity Index (ESI, 1–5)** from vitals and
chief-complaint data captured at triage. It is decision-support, not automation: it
surfaces an acuity recommendation for a clinician to confirm or override, and runs as
a passive background layer *after* paper-to-EHR transcription — respecting the
Caribbean ED workflow documented by De Freitas et al. (2020).

## 2. Clinical Context

EDs require rapid triage under pressure, where human variance drives roughly a
1-in-6 inter-rater disagreement rate (Picard, 2023) and missing vitals make standard
triage models fragile (Eriten, 2024). This project targets both problems in a
resource-constrained setting, evaluated on synthetic Caribbean-modelled data in an
isolated environment so no live patient care is affected.

## 3. How to Run the Final Model

The pinned model and reproducible pipeline live at the repo root (Week 8 work):

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    # place the dataset at data/yaleemmlc_admissionprediction_triage.csv
    python scripts/train.py --config config.yaml      # train + evaluate the pinned model
    pytest -q                                          # run sanity checks

All settings — paths, seed, model, hyperparameters — live in `config.yaml`.
Full handover: `docs/HANDOVER.md`. Model comparison: `docs/model-selection.md`.

## 4. Repository Structure

    src/          modular pipeline: data.py, features.py, model.py, utils.py
    scripts/      train.py (entry point), benchmark.py (rebuilds results table)
    tests/        pytest sanity checks (schema + training smoke test)
    config.yaml   single source of truth for the pinned model
    docs/         handover, model-selection table, memos
    notebooks/    exploratory Week 5–7 notebooks (preserved originals)
    data/         dataset lives here locally (not committed — see governance)
    Week-0 … Week-7   weekly deliverables and interim submissions

## 5. Week-by-Week Map

| Week | Focus | Key deliverable |
|---|---|---|
| 0 | Project kickoff & first dataset | Initial notebook and problem framing |
| 1 | Research framing & literature | Proposal + 7-source literature review, gap analysis |
| 2 | Project setup & documentation | Repo structure, Git branch/PR workflow, reference manager |
| 3 | Triage workflow | ED triage workflow mapping |
| 4 | Consolidated proposal | Interim submission / consolidated proposal |
| 5 | Clinical data literacy | Data profiling of the 225-feature ED dataset |
| 6 | Baseline model | Logistic regression + decision tree, model evaluation |
| 7 | Optimisation & trade-offs | Cost-benefit memo + decision journal → **Random Forest** chosen |
| 8 | Reproducibility & handover | Modular `src/` refactor, config, results table, handover doc |

## 6. Final Model Decision

The Week 7 decision journal recommends the **Random Forest** as the Phase 3 triage
model, with logistic regression retained as the documented fallback. It was chosen for
the best ESI-1 recall (0.500) and macro recall (0.553) while staying interpretable
enough for clinical governance — the ESI-1 axis matters most, since under-triage of a
critical patient is the error to avoid. Full reasoning:
`Week-7/Decision Journal_ Week 7 Model Choice.pdf`.

## 7. Data & Governance

The clinical dataset is **not committed** to this repo. It lives locally in `data/`.
Access is governed by the Mercer Research Ethics Committee; the extract is
de-identified, and fairness-sensitive fields (race, ethnicity, language, religion,
insurance) are excluded from the baseline feature set by default.

## 8. Licence

Educational use only, under the terms in `LICENSE`. Not for public redistribution or
clinical deployment.
