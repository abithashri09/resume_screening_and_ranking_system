# resume_screening_and_ranking_system
# Project Overview

The AI Resume Screening and Ranking System is designed to automate the resume screening process by extracting candidate information from resumes, comparing it with job descriptions, ranking candidates based on their suitability, and generating AI-powered insights for recruiters.

---
# Technologies Used

- Python
- Streamlit
- PyPDF
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- BERT
- Ollama
- Llama 3.2
- LangChain
- Regular Expressions (Regex)

---

#  Week 1 – Basic ML Scoring

### Objective
Develop a basic Machine Learning model to score resumes based on their relevance to a job description.

### Work Completed
- Collected and explored the resume dataset.
- Cleaned and preprocessed the dataset.
- Converted resume text into numerical features using **TF-IDF Vectorization**.
- Trained a Machine Learning model to predict resume matching scores.
- Saved the trained model and vectorizer for future use.

### Technologies Used
- Scikit-learn
- TF-IDF Vectorizer
- Python

---

# Week 2 – Resume Parsing, Feature Extraction & Scoring Logic Development

### Objective
Extract useful information from PDF resumes and develop the resume scoring logic.

### Work Completed
- Built a PDF Resume Parser using **PyPDF**.
- Extracted resume text from uploaded PDF files.
- Extracted candidate details such as:
  - Name
  - Email
  - Phone Number
  - Skills
- Created a predefined skills database.
- Compared extracted skills with the Job Description.
- Calculated:
  - Resume Match Score
  - Matched Skills
  - Missing Skills
- Displayed the results in a Streamlit dashboard.

### Technologies Used
- PyPDF
- Regex
- Streamlit
- Python

---

#  Week 3 – CNN for Resume Layout/Image Analysis (Optional)

### Objective
Study how Convolutional Neural Networks (CNNs) can be used to analyze resume layouts and visual structure.

### Work Completed
- Explored the concept of CNNs for document image analysis.
- Understood how resume layouts can be classified using deep learning.
- Learned how CNNs can help identify resume sections, formatting, and document structure for future improvements.

### Technologies Studied
- CNN
- Deep Learning
- Computer Vision

---

#  Week 4 – BERT for Skill Extraction & Experience Matching

### Objective
Improve resume screening by using BERT for semantic understanding.

### Work Completed
- Studied BERT for Natural Language Processing.
- Used BERT to understand the context of resume content instead of relying only on keyword matching.
- Improved skill extraction.
- Improved experience matching between resumes and job descriptions.
- Enhanced the overall resume ranking process.

### Technologies Used
- BERT
- NLP
- Python

---

#  Week 5 – LLM for Candidate Summary & Interview Question Generation

### Objective
Integrate a Large Language Model (LLM) to generate intelligent recruiter insights.

### Work Completed
- Integrated **Ollama** with **Llama 3.2**.
- Generated AI-powered candidate summaries.
- Generated technical interview questions based on the candidate's resume.
- Displayed AI-generated insights in the Streamlit dashboard.

### Technologies Used
- Ollama
- Llama 3.2
- LangChain
- Streamlit

---

#  Final Features

- Upload Resume (PDF)
- Resume Parsing
- Candidate Information Extraction
- Skill Extraction
- Resume Match Score
- Matched & Missing Skills
- Resume Ranking
- Semantic Matching using BERT
- AI Candidate Summary
- AI Interview Question Generation

---

# Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama serve
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# Developed By

**Abitha Shri**

Computer Science Engineering Student
