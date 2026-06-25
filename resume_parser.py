import re
from skills import SKILLS_DATABASE

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group() if match else "Not Found"

def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group() if match else "Not Found"

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DATABASE:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))