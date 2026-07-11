import re
from parser.skills import SKILLS

def extract_resume_info(text):
    info = {}

    name = text.split("\n")[0].strip()
    info["Name"] = name

    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    info["Email"] = email[0] if email else "Not Found"

    phone = re.findall(r'\+?\d[\d\s\-]{8,15}', text)
    info["Phone"] = phone[0] if phone else "Not Found"

    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    info["Skills"] = found_skills

    return info