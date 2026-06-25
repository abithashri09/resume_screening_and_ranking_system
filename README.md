# Resume Screening and Ranking System

## Week 1 Task

Developed a basic machine learning model to score resumes.

- Predict candidate scores based on:
  - Skills
  - Experience
  - Education
- Use the predicted score for candidate evaluation.

## Dataset

**Dataset Name:** candidates.csv

- Total Records: 10
- Features:
  - Skills (1–10)
  - Experience (Years)
  - Education Level
    - 1 = UG
    - 2 = PG
    - 3 = PhD
- Target Variable:
  - Resume Score

## Technologies Used

- Python
- Pandas
- Scikit-learn
- VS Code
- GitHub

## Machine Learning Model

- Model Used: Linear Regression
- Purpose: Predict resume scores

## Model Performance

- Train-Test Split: 80% – 20%
- Evaluation Metric: R² Score
- Accuracy: Approximately 90–95%

## Conclusion

- Successfully built a resume scoring model.
- Predicted candidate scores based on input features.
- Achieved good prediction accuracy.


# Week 2: Resume Parsing, Feature Extraction, and Scoring Logic Development

## Objective

To automate resume screening by extracting candidate information, identifying relevant skills, and calculating a resume-job match score.

## Implementation

- Developed a resume parser using Python
- Extracted candidate details such as Name, Email, Phone Number, Skills, and Education
- Implemented feature extraction using Natural Language Processing (NLP)
- Matched candidate skills with job requirements
- Developed a scoring algorithm to rank resumes based on relevance
- Generated resume match percentage for candidate evaluation

## Results

### Extracted Information:

- Name: Successfully extracted
- Email: Successfully extracted
- Phone Number: Successfully extracted
- Skills: Identified and categorized
- Education: Parsed from resume text

### Resume Scoring:

- Skill Matching Accuracy: High
- Resume Ranking: Successfully generated
- Match Score Range: 0–100%

## Conclusion

The resume parsing system successfully extracted important candidate information.

The feature extraction process identified relevant skills and qualifications, while the scoring logic provided an effective method for ranking resumes against job requirements.

