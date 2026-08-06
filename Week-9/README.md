# Week 9 - HCI, Co-Design and Prototyping

**Project:** CariSurg AI Emergency Care Platform (AI Emergency Triage)
**Deployment context:** Mercer General Hospital, Emergency Department
**Setting chosen:** Screen based / Human and Computer Interaction (HCI)
**Author:** Shakada Blake

**Live prototype:** https://ai-triage.tiiny.site/  (open in any browser, no install)

This folder contains the four Week 9 artefacts. Each file below maps to one rubric criterion.

The whole Week 9 design is grounded in the model I built in Weeks 5 to 8: it predicts the ESI triage level (1 to 5) from triage vitals and chief complaint flags, holds out demographics for fairness, removes outcome columns as leakage, and is judged above all on recall for ESI 1. See `Week9_Model_Card.md` for the full summary and the source notebooks.

---

## 1. Draft Co-Design Canvas  (rubric item 1)
**File:** `Week9_CoDesign_Canvas_HCI.docx`

An HCI co-design canvas for the AI triage platform. The three graded sections are filled substantively and specific to the setting:

- **Problem** names the actual clinical workflow: door to disposition triage at Mercer General ED, paper first vitals capture, the record lag, hand managed queue under surge, and blank field fragility.
- **Environment** names physical and workflow constraints: scarce attention under surge, no bedside terminals, connectivity and power drops, integrating on top of an older record, and mobile and security limits.
- **Ethics** names domain specific concerns: automation bias and the Friction Protocol, explainability, alert fatigue, missing data safety, patient consent and permissioned sharing, equity audits, accountability and governance (Data Protection Act 2023, WHO 2021), and model monitoring.

---

## 2. Initial Mock-Up Sketches  (rubric item 2)
**Files:** `Week9_Mockup_AITriagePlatform.png` and `Week9_Mockup_AITriagePlatform_Sections.png`

Both depict the required triage related interaction: a **live queue view with colour coded alert states** (Critical, High, Moderate, Hold), with AI risk scores, confidence, suggested investigations, recommended pathways, and a progression timeline.

- `Week9_Mockup_AITriagePlatform.png` is the single integrated hero view.
- `Week9_Mockup_AITriagePlatform_Sections.png` is the same platform shown as a labelled product tour (triage, menu, patient portal, clinician network, administration).
- The `*_source.html` files are the editable sources used to render the images.

---

## 3. Inputs/Outputs Integration Notes  (rubric item 3)
**File:** `Week9_Integration_Notes_Inputs_Outputs.docx`

- **(a) Inputs the platform receives:** manual entry, record pull, patient uploads, permissioned partner shares, and future device streams.
- **(b) Outputs the platform emits:** an AI ordered queue, colour coded urgency states, a deterioration risk number and AI confidence, suggested investigations and pathway, and a copilot action, with no autonomous routing.
- **(c) What the human does next:** the nurse scores first, reviews the drivers and confidence, confirms or overrides, handles the hold state, and makes the final routing decision.

---

## 4. Repo Discipline and Committed Artefacts  (rubric item 4)
All artefacts sit in this folder with clear names. This README maps each file to its rubric criterion so a reviewer can identify every artefact without opening it.

| File | Artefact |
|------|----------|
| `Week9_CoDesign_Canvas_HCI.docx` | Co-design canvas |
| `Week9_Mockup_AITriagePlatform.png` | Mock-up (integrated view) |
| `Week9_Mockup_AITriagePlatform_Sections.png` | Mock-up (sectioned product tour) |
| `Week9_Integration_Notes_Inputs_Outputs.docx` | Inputs and outputs integration notes |
| `Week9_Model_Card.md` | Summary of the Weeks 5 to 8 model behind the design |
| `Week9_Prototype_AITriage.html` | Working interactive prototype |
| `LICENSE.md` | Proprietary licence, owner Shakada Blake |
| `Week9_Regulatory_Alignment.md` | Privacy and regulation alignment (Grenada DPA 2023) |
| `*_source.html` | Editable sources for the mock-up images |

## Ownership, licence and compliance
- **Owner and administrator:** Shakada Blake. The work is released under a proprietary, all rights reserved licence (`LICENSE.md`). The author name is watermarked in the prototype background, embedded in the code as copyright headers, and printed on the mock-up images.
- **Regulation:** `Week9_Regulatory_Alignment.md` maps the design to the Grenada Data Protection Act 2023, WHO 2021 AI ethics, and HIPAA style safeguards as a benchmark. HIPAA is a United States law and does not apply in Grenada; it is used only as a good practice bar. This is a design level alignment, not a certification. A Data Protection Impact Assessment and legal sign off are required before any use with real patient data. The prototype uses synthetic patients only.

## Model and code (Weeks 5 to 8)
**File:** `Week9_Model_Card.md`

Describes the real model the Week 9 design is built on: the Yale EMMLC triage extract, the ESI target, the exact feature groups used and the demographics and leakage columns held out, the models (logistic regression and decision tree, then tuned gradient boosting, random forest and a small MLP), and the priority metric of recall for ESI 1. It points to the project notebooks (Weeks 5, 6 and 7) that contain the code.

## Bonus: Working Prototype
**File:** `Week9_Prototype_AITriage.html` &nbsp; · &nbsp; **Live:** https://ai-triage.tiiny.site/

A self contained, clickable prototype (open it in any browser, no install). It has working navigation across all screens and the full triage flow: the nurse enters their own score first, the AI recommendation then reveals with risk, confidence and drivers, and the nurse confirms or overrides with a logged reason. It also demonstrates the missing data safety hold and the permission based record unlock.
