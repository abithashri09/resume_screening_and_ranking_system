from resume_parser import (
    extract_email,
    extract_phone,
    extract_skills
)

from scoring import calculate_score

with open("resumes/sample_resume.txt", "r") as file:
    resume_text = file.read()

email = extract_email(resume_text)
phone = extract_phone(resume_text)
skills = extract_skills(resume_text)

required_skills = [
    "python",
    "sql",
    "machine learning",
    "tableau"
]

score, matched_skills = calculate_score(
    skills,
    required_skills
)

print("\n----- Resume Analysis -----")
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills)

print("\nMatched Skills:", matched_skills)
print("Resume Score:", score, "%")