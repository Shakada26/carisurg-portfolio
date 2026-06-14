# CariSurg MedTech Pathways Programme – Week 0 Portfolio

## Student Information
Name: Shakada Blake  
Programme: CariSurg MedTech Pathways Cohort 2026  
Start Date: May 2026  

---

# Project Overview

This repository contains my Week 0 portfolio and foundational clinical AI tasks completed during the CariSurg MedTech Pathways Programme.

The purpose of Week 0 is to:
- establish my technical environment,
- develop familiarity with Google Colab and GitHub,
- practice cleaning clinical data,
- and begin building a professional portfolio in clinical AI and healthcare technology.

The dataset used is a reduced and de-identified emergency department triage dataset containing patient demographic information and vital signs.

---

# Dataset Information

The project utilised a reduced and de-identified emergency department triage dataset containing demographic information and vital signs for educational and portfolio development purposes within the CariSurg MedTech Pathways Programme.

Due to educational usage restrictions, the original dataset source is not publicly distributed within this repository.

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

---

# Day 5 – Missing Clinical Variables in Emergency Triage Dataset (Blood Glucose, Pain Score, Weight, Chief Complaint)

The emergency department triage dataset contains key physiological vital signs such as pulse, temperature, respiratory rate, blood pressure, and oxygen saturation. However, several clinically important variables are missing that are essential for complete patient assessment and accurate triage decision-making.

From my perspective as a medical assistant, the most important missing variable is blood glucose level, which is critical for identifying acute metabolic emergencies such as hypoglycemia, diabetic ketoacidosis (DKA), and hyperosmolar hyperglycemic state (HHS). These conditions may present with non-specific symptoms and may not be immediately reflected in basic vital signs.

Another key missing variable is pain score (0–10 scale). Pain is a clinically significant indicator of underlying pathology and is routinely used in emergency departments to identify potential surgical or vascular emergencies such as appendicitis, renal colic, torsion, and abdominal aortic aneurysm.

Patient weight is also an important clinical factor that is not included in the dataset. It is required for medication dosing, fluid resuscitation calculations, and accurate physiological interpretation in emergency care settings.

In addition, chief complaint is a critical missing component. Vital signs alone do not provide clinical context, and the reason for presentation is essential for correct interpretation. For example, tachycardia may be caused by anxiety in one patient but may indicate sepsis, hemorrhage, or pulmonary embolism in another.

Including these additional variables would improve clinical decision-making, strengthen triage accuracy, and enhance the predictive performance of AI-driven healthcare systems by combining physiological data with essential clinical context.

---

# Day 6 – Digital Triage Workflow & Pseudocode Design

For Day 6, I designed a simplified digital triage workflow demonstrating how patient vital signs can be processed within an AI-assisted emergency department system.

The task focused on creating:
- pseudocode logic,
- clinical decision pathways,
- and a visual flowchart representing the triage process.

The workflow evaluates:
- oxygen saturation (SpO₂),
- pulse rate,
- and temperature

to categorise patients into:
- High Risk
- Moderate Risk
- Low Risk

The flowchart was developed using Python and Graphviz in Google Colab to simulate how digital healthcare systems support triage prioritisation and clinical decision-making.

## Skills Practiced
- Pseudocode design
- Clinical workflow modelling
- Graphviz flowchart development
- AI-assisted healthcare reasoning
- Emergency triage system design
  
---

# Workflow Summary

Throughout Week 0, the project progressed from foundational data cleaning and preprocessing to exploratory analysis, clinical interpretation, and finally digital triage workflow design.

This workflow demonstrates the integration of healthcare analytics, clinical reasoning, and AI-assisted system modelling within an emergency medicine context.

---

# Repository Contents

| File                                     | Description                                                                                                                               |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| day1_gender_cleaning.ipynb               | Cleaning and standardisation of the Gender column using pandas categorical mapping and preprocessing techniques                           |
| day2_temperature_cleaning.ipynb          | Clinical preprocessing and validation of Temperature vital sign data, including numeric conversion and outlier removal                    |
| day3_data_visualization.ipynb            | Exploratory Data Analysis (EDA) using histograms and scatter plots for Pulse and Age, including tachycardia threshold visualization       |
| day4_pulse_clinical_interpretation.ipynb | Clinical interpretation of Pulse as a vital sign, including normal ranges, tachycardia, bradycardia, and emergency triage significance    |
| day5_missing_variables_analysis.ipynb    | Clinical critique of missing variables in the emergency triage dataset including glucose, pain score, patient weight, and chief complaint |
| day6_triage_workflow.ipynb               | Digital triage workflow design using pseudocode, clinical logic, and Graphviz flowchart modelling                                         |
| a4_ai_flowchart.png                      | Visual AI-assisted emergency department triage workflow flowchart created using Python and Graphviz                                       |
| task5_final_notebook.ipynb               | Final integrated notebook combining Week 0 tasks, documentation, clinical workflow logic, and portfolio deliverables                      |
| README.md                                | Full Week 0 portfolio documentation, project overview, work                                                                               |                                                                          

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
Week 2: feature branch created for repository refactor and audit workflow.


# Author

Shakada Blake  
CariSurg MedTech Pathways Cohort 2026
