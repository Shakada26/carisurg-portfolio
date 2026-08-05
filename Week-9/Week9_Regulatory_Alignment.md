# Regulatory Alignment and Privacy Safeguards (design level)

**Owner and Administrator:** Shakada Blake
**Copyright © 2026 Shakada Blake. All rights reserved.**

## Read this first (important framing)
This document shows how the CariSurg design **aligns with** privacy and safety
regulations. It is **not** a certificate of compliance. A prototype cannot be
compliant on its own. Before any use with real patient data, the project needs a
**Data Protection Impact Assessment (DPIA)**, a security review, model validation,
a bias audit, and sign-off from a **Data Protection Officer** and legal counsel.
Compliance is a process, not a checkbox.

**Jurisdiction note.** HIPAA is a **United States** law and does **not** apply in
Grenada. The governing law for this project is **Grenada's Data Protection Act,
2023**. HIPAA is used here only as a well known **benchmark of good practice**,
alongside the **WHO 2021** guidance on the ethics and governance of AI for health.

The prototype in this repository uses **synthetic and example patients only**. It
holds no real patient data, uses no servers, and stores nothing in the browser.

---

## A. Grenada Data Protection Act 2023 — how the design aligns
- **Lawful basis and purpose limitation.** Data is processed only to support
  triage decisions. It is not repurposed for anything else.
- **Data minimisation.** The model uses triage vitals and chief complaint flags
  only. Demographics are deliberately excluded, so less personal data is processed.
- **Consent and data subject rights.** The patient portal gives patients access to
  their own results and records. Sharing through the clinician network is blocked
  until the patient authorises it.
- **Security safeguards.** The design calls for encryption in transit and at rest,
  role based access control, and a full audit log of who saw and changed what.
- **Accountability.** A named data controller and Data Protection Officer, a
  retention and deletion schedule, and an auditable trail of decisions.
- **Cross border transfer.** Any sharing outside Grenada would need its own lawful
  basis and safeguards, and is out of scope for the pilot.

## B. HIPAA style safeguards (best practice benchmark, not a legal obligation here)
- **Administrative safeguards.** Access policies, staff training, an override
  policy, and a named security officer.
- **Physical safeguards.** Controlled workstations and devices in the department.
- **Technical safeguards.** Unique user IDs, access controls, audit controls,
  data integrity checks, and transmission security (encryption).
- **Minimum necessary.** Each role sees only the data it needs.
- **Note.** The HIPAA covered entity and business associate framework is specific
  to the United States. It is treated here as a quality bar, not a local rule.

## C. WHO 2021 ethics and governance of AI for health
- **Human oversight.** The Friction Protocol keeps the nurse in charge; the AI
  advises and never routes or orders on its own.
- **Transparency and explainability.** Every flag shows its top drivers in plain
  English with a confidence level, readable in under 60 seconds.
- **Fairness.** Demographics are held out of the model to reduce unfair bias, and
  ordering is audited across patient groups.
- **Safety.** Recall for ESI 1 is the priority metric, and predictions pause on
  missing critical data rather than guessing.
- **Accountability.** Clinicians keep final authority and every action is logged.

## D. Data handling in the prototype itself
- Synthetic and example patients only. No real patient data.
- No servers, no accounts, no browser storage. It runs fully on the device.
- Before real data is ever used: DPIA, security review, validation, bias audit,
  and DPO and legal approval.

## E. Ownership and administration
The owner and administrator of this system and all its artefacts is
**Shakada Blake**. See `LICENSE.md`. Author watermarks are embedded in the code and
images as evidence of authorship.
