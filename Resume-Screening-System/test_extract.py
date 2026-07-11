from parser.pdf_reader import extract_text
from parser.extract_info import extract_resume_info

pdf_path = "data/resumes/resume1.pdf"

text = extract_text(pdf_path)

info = extract_resume_info(text)

print("\nResume Information")
print("-" * 40)

for key, value in info.items():
    print(f"{key}: {value}")