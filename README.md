# CariSurg MedTech Pathways Programme – Week 0

## Student Information
**Name:** Shakada Blake  
**Programme:** CariSurg MedTech Pathways Cohort 2026  
**Start Date:** May 2026  

---

# Project Overview

This repository contains my Week 0 onboarding tasks for the CariSurg MedTech Pathways Programme.

The purpose of Week 0 is to:
- establish my technical environment,
- develop familiarity with Google Colab and GitHub,
- practice cleaning clinical data,
- and begin building a professional portfolio in clinical AI and healthcare technology.

The dataset used is a reduced and de-identified emergency department triage dataset containing patient demographic information and vital signs.

---

# Day 0 – Environment Setup

During Day 0, I completed the initial setup for the programme by:
- creating a Google Colab environment,
- linking Google Drive,
- confirming Python 3.10+ functionality,
- creating a public GitHub repository,
- and learning the workflow for uploading and managing notebooks.

### Tools Used
- Google Colab
- Google Drive
- GitHub
- Python

---

# Day 1 – Gender Column Cleaning

For Day 1, I cleaned the `Gender` column using Python and pandas.

### Method Used
The dataset contained inconsistent values including:
- `Male`
- `MALE`
- `Female`
- `FEMALE`
- `0`
- `1`

To standardize the data:
1. String formatting was normalized using uppercase conversion.
2. Extra whitespace was removed.
3. Different gender representations were mapped into consistent labels:
   - `Male`
   - `Female`

### Skills Practiced
- Data cleaning
- Categorical variable standardization
- pandas preprocessing
- Dataset validation

---

# Day 2 – Temperature Vital Sign Cleaning

For Day 2, I selected the `Temperature` vital sign column for cleaning and preprocessing.

### Method Used
The following preprocessing steps were performed:
1. Temperature values were converted into numeric format using pandas.
2. Missing or invalid values were identified.
3. Unrealistic temperature readings outside the normal physiological range were removed.
4. Summary statistics were reviewed using `.describe()`.

### Cleaning Threshold
Normal human temperature ranges were constrained approximately between:

30°C ≤ Temperature ≤ 45°C

### Skills Practiced
- Clinical data preprocessing
- Numeric data cleaning
- Missing value identification
- Outlier filtering
- Exploratory preparation

---

# Repository Contents

| File | Description |
|---|---|
| `day1_gender_cleaning.ipynb` | Gender column cleaning notebook |
| `day2_temperature_cleaning.ipynb` | Temperature cleaning notebook |
| `README.md` | Week 0 documentation and project overview |

---

# Programme Goals

This programme aims to build foundational skills in:
- Clinical AI
- Healthcare data analysis
- Research communication
- Technical portfolio development
- AI-assisted workflow development

---

# Author
Shakada Blake
