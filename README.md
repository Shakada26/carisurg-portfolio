# CariSurg MedTech Pathways Programme – Week 0

## Student Information
Name: Shakada Blake  
Programme: CariSurg MedTech Pathways Cohort 2026  
Start Date: May 2026  

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

## Tools Used
- Google Colab
- Google Drive
- GitHub
- Python

---

# Day 1 – Gender Column Cleaning

For Day 1, I cleaned the Gender column using Python and pandas.

## Method Used

The dataset contained inconsistent values including:
- Male
- MALE
- Female
- FEMALE
- 0
- 1

To standardize the data:
1. String formatting was normalized using uppercase conversion.
2. Extra whitespace was removed.
3. Different gender representations were mapped into consistent labels:
   - Male
   - Female

## Skills Practiced
- Data cleaning
- Categorical variable standardization
- pandas preprocessing
- Dataset validation

---

# Day 2 – Temperature Vital Sign Cleaning

For Day 2, I selected the Temperature vital sign column for cleaning and preprocessing.

## Method Used

The following preprocessing steps were performed:
1. Temperature values were converted into numeric format using pandas.
2. Missing or invalid values were identified.
3. Unrealistic temperature readings outside the normal physiological range were removed.
4. Summary statistics were reviewed using `.describe()`.

## Cleaning Threshold

30°C ≤ Temperature ≤ 45°C

## Skills Practiced
- Clinical data preprocessing
- Numeric data cleaning
- Missing value identification
- Outlier filtering
- Exploratory preparation

---

# Day 3 – Clinical Data Visualization

For Day 3, I performed exploratory data visualization on the emergency triage dataset using Python and matplotlib in Google Colab. I selected the Pulse column because pulse rate is an important clinical vital sign used to assess cardiovascular stability and patient condition in emergency medicine.

## Visualizations Created
- Histogram of Pulse distribution
- Scatter plot of Pulse vs Age
- Clinical tachycardia threshold visualization

## Method Used

The Pulse and Age columns were converted into numeric format using pandas to ensure accurate plotting and analysis. Missing values were removed before visualization. A histogram was created to observe the overall distribution of pulse readings across patients, while a scatter plot was used to examine how pulse values vary with age.

To make the analysis more clinically meaningful, I added a tachycardia threshold line at 100 bpm to highlight potentially abnormal pulse readings. This approach helps identify trends, outliers, and possible at-risk patients within the dataset.

## Skills Practiced
- Data visualization
- Exploratory Data Analysis (EDA)
- Clinical data interpretation
- matplotlib plotting
- Healthcare analytics reasoning

---

# Day 4 – Clinical Vital Sign Interpretation

For Day 4, I selected Pulse as the vital sign for clinical interpretation because it is a critical indicator of cardiovascular and hemodynamic stability in emergency medicine.

Pulse rate, clinically referred to as heart rate, represents the number of ventricular contractions occurring per minute and serves as a fundamental indicator of cardiovascular and hemodynamic function. In the adult population, the normal resting pulse range is generally accepted as 60–100 beats per minute (bpm). A pulse exceeding 100 bpm is classified as tachycardia and may be associated with pyrexia, hypovolemia, dehydration, infection, anemia, pain, anxiety, or underlying cardiac dysrhythmias. Conversely, a pulse below 60 bpm is considered bradycardia and may occur secondary to conduction abnormalities, pharmacological agents such as beta-blockers, hypothyroidism, or increased vagal tone in highly conditioned individuals. Within the emergency triage setting, pulse assessment is clinically significant because deviations from the normal range may indicate early physiological deterioration, circulatory compromise, or systemic instability, thereby assisting healthcare professionals in prioritizing patient acuity, initiating timely intervention, and guiding escalation of care.

## Clinical Ranges
- Normal Pulse: 60–100 bpm
- Tachycardia: >100 bpm
- Bradycardia: <60 bpm

## Clinical Importance
Pulse abnormalities may indicate cardiovascular compromise, infection, hypovolemia, physiological stress, or systemic instability. Continuous pulse monitoring during triage assists healthcare professionals in rapidly identifying patients who may require urgent intervention or escalation of care.

---


# Repository Contents

| File | Description |
|---|---|
| `day1_gender_cleaning.ipynb` | Gender column cleaning notebook |
| `day2_temperature_cleaning.ipynb` | Temperature vital sign cleaning notebook |
| `day3_data_visualization.ipynb` | Clinical data visualization notebook containing histogram and scatter plot analysis |
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

# Future Goals

As the programme progresses, this repository will continue to expand with additional clinical AI projects, data analysis tasks, and healthcare technology workflows developed throughout the CariSurg MedTech Pathways Programme.

---

# Author

Shakada Blake  
CariSurg MedTech Pathways Cohort 2026
