from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0.3
)


def candidate_summary(resume_text):

    prompt = f"""
You are an AI Recruiter.

Analyze the following resume.

Return:

1. Professional Summary
2. Candidate Strengths
3. Candidate Weaknesses
4. Suitable Job Roles
5. Five Technical Interview Questions

Resume:

{resume_text}
"""

    response = llm.invoke(prompt)

    return response.content