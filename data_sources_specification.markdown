# Data Sources Specification for VR Sign Language Learning Evaluation

## Overview

This document outlines the data sources used to evaluate the effectiveness of the VR sign language learning application, as specified in the evaluation plan. The primary data source is a simulated dataset, "student_data.csv," representing responses from 100 deaf primary students. This dataset includes demographic details, pre-test and post-test scores, and reaction data aligned with the Kirkpatrick model's Level 1 (Reaction) and Level 2 (Learning). Secondary data sources include qualitative insights from student and educator interviews.

---

## 1. Primary Data Source: student_data.csv

### 1.1 File Structure and Content
- **File Name**: student_data.csv  
- **Sample Size**: 100 deaf primary students  
- **Data Types**: Quantitative (numeric and categorical)  
- **Purpose**: Simulate data collection for evaluation analysis  

### 1.2 Data Categories and Columns
The "student_data.csv" file includes the following columns:

#### A. Demographic Data
- **Student_ID**: Unique identifier (e.g., S001 to S100)  
- **Age**: Student age (numeric, range: 6-12)  
- **Gender**: Student gender (categorical: Male, Female, Other)  
- **Grade_Level**: Current grade (numeric: 1-6)  

#### B. Pre-test Data (Baseline Assessment)
- **Pre_Sign_Vocabulary_Score**: Vocabulary knowledge before VR (numeric: 0-100)  
- **Pre_Comprehension_Score**: Comprehension ability before VR (numeric: 0-100)  
- **Pre_Production_Score**: Production skill before VR (numeric: 0-100)  

#### C. Post-test Data (Post-Intervention Assessment)
- **Post_Sign_Vocabulary_Score**: Vocabulary knowledge after VR (numeric: 0-100)  
- **Post_Comprehension_Score**: Comprehension ability after VR (numeric: 0-100)  
- **Post_Production_Score**: Production skill after VR (numeric: 0-100)  

#### D. Reaction Data (Kirkpatrick Level 1)
- **VR_Satisfaction_Overall**: Overall satisfaction with VR (Likert scale: 1-5)  
- **VR_Ease_of_Use**: Ease of using VR (Likert scale: 1-5)  
- **VR_Engagement_Level**: Engagement level with VR (Likert scale: 1-5)  
- **VR_Recommendation**: Likelihood to recommend VR (Likert scale: 1-5)  

### 1.3 Dummy Data Creation
The dummy data was generated to reflect realistic scenarios:
- **Student_ID**: Sequential identifiers (S001 to S100).  
- **Age**: Randomly assigned between 6 and 12, following a uniform distribution.  
- **Gender**: Randomly assigned (e.g., 50% Male, 45% Female, 5% Other).  
- **Grade_Level**: Mapped to age (e.g., 6-year-olds in Grade 1, 12-year-olds in Grade 6).  
- **Pre-test Scores**: Random scores between 20-80, simulating varied baseline abilities.  
- **Post-test Scores**: Pre-test scores increased by 10-30 points (with variability), reflecting learning gains.  
- **Reaction Data**: Ratings between 3-5, skewed positively to simulate favorable responses.  

**Example Rows**:
```
Student_ID,Age,Gender,Grade_Level,Pre_Sign_Vocabulary_Score,Pre_Comprehension_Score,Pre_Production_Score,Post_Sign_Vocabulary_Score,Post_Comprehension_Score,Post_Production_Score,VR_Satisfaction_Overall,VR_Ease_of_Use,VR_Engagement_Level,VR_Recommendation
S001,8,Female,3,45,50,40,70,75,65,4,5,4,4
S002,10,Male,5,60,55,50,85,80,75,5,4,5,5
S003,6,Other,1,30,35,25,50,55,45,3,4,4,3
```

---

## 2. Secondary Data Sources

### 2.1 Student Interview Data
- **Method**: Semi-structured interviews  
- **Sample Size**: 20-30 students (subset of 100)  
- **Format**: Transcribed text from simulated interviews  
- **Purpose**: Capture qualitative feedback on VR experience  
- **Linkage**: Tied to Student_ID for integration with CSV data  

### 2.2 Educator Interview Data
- **Method**: In-depth interviews  
- **Sample Size**: 8-10 educators  
- **Format**: Transcribed text from simulated interviews  
- **Purpose**: Provide professional insights on VR effectiveness  

---

## 3. Data Integration and Usage
- **Quantitative Analysis**: Use "student_data.csv" for statistical tests (e.g., paired t-tests) to compare pre/post scores and assess reaction metrics.  
- **Qualitative Support**: Interview data contextualizes quantitative results, identifying themes like usability and engagement.  
- **Evaluation Alignment**: Supports Kirkpatrick Level 1 (reaction ratings) and Level 2 (learning gains).  

---

## 4. Ethical Considerations (Simulated)
- **Anonymity**: Student_IDs anonymize participants.  
- **Data Security**: Simulated secure storage protocols.  
- **Consent**: Assumed parental consent and student assent.  

---

## 5. Limitations
- **Simulated Data**: Lacks real-world noise and complexity.  
- **No Control Group**: Limits causal conclusions.  
- **Bias**: Positive skew in reaction data may not reflect all scenarios.  

---

This specification ensures the "student_data.csv" dummy dataset and secondary sources provide a robust foundation for evaluating the VR sign language learning application, meeting the evaluation plan's objectives.