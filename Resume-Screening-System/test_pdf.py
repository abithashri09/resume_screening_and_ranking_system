import os
from pypdf import PdfReader

resume_folder = "data/resumes"

pdf_files = [f for f in os.listdir(resume_folder) if f.endswith(".pdf")]

pdf_path = os.path.join(resume_folder, pdf_files[0])

reader = PdfReader(pdf_path)

print("Number of pages:", len(reader.pages))

for i, page in enumerate(reader.pages):
    text = page.extract_text()

    print(f"\nPage {i+1}")
    print("Length:", 0 if text is None else len(text))

    if text:
        print(text[:500])