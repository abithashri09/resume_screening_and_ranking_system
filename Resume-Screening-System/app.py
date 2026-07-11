import streamlit as st
from parser.pdf_reader import extract_text
from parser.extract_info import extract_resume_info
from llm.summary import candidate_summary

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Ranking System")

st.write("Upload a resume and compare it with the Job Description using Machine Learning + LLM.")

st.divider()

# ------------------------------
# Upload Resume
# ------------------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ------------------------------
# Job Description
# ------------------------------
jd = st.text_area(
    "Paste Job Description",
    height=200
)

# ------------------------------
# Process Resume
# ------------------------------
if uploaded_file is not None:

    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract Resume Text
    text = extract_text("temp_resume.pdf")

    # Extract Candidate Information
    info = extract_resume_info(text)

    # Generate AI Summary
    with st.spinner("Analyzing Resume using Llama 3..."):
        summary = candidate_summary(text)

    # ------------------------------
    # Candidate Information
    # ------------------------------
    st.header("👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Name", info["Name"])
        st.metric("Email", info["Email"])

    with col2:
        st.metric("Phone", info["Phone"])
        st.metric("Total Skills", len(info["Skills"]))

    st.divider()

    # ------------------------------
    # Skills
    # ------------------------------
    st.header("🛠 Extracted Skills")

    if len(info["Skills"]) > 0:

        cols = st.columns(3)

        for i, skill in enumerate(info["Skills"]):
            cols[i % 3].success(skill)

    else:
        st.warning("No skills detected.")

    st.divider()

    # ------------------------------
    # Resume Matching
    # ------------------------------
    if jd.strip():

        jd = jd.lower()

        matched = []
        missing = []

        # Match skills
        for skill in info["Skills"]:

            if skill.lower() in jd:
                matched.append(skill)

        # Missing Skills
        jd_words = jd.replace(",", " ").split()

        for word in jd_words:

            if (
                word not in [s.lower() for s in info["Skills"]]
                and len(word) > 2
            ):
                missing.append(word)

        missing = sorted(list(set(missing)))

        # Match Score
        if len(info["Skills"]) > 0:
            score = int((len(matched) / len(info["Skills"])) * 100)
        else:
            score = 0

        st.header("📊 Resume Match Score")

        st.progress(score / 100)

        st.metric("Match Score", f"{score}%")

        col1, col2 = st.columns(2)

        with col1:

            st.success("✅ Matched Skills")

            if matched:
                for skill in matched:
                    st.write("✔", skill)
            else:
                st.write("No matched skills")

        with col2:

            st.error("❌ Missing Skills")

            if missing:
                for skill in missing:
                    st.write("•", skill)
            else:
                st.write("No missing skills")

    st.divider()

    # ------------------------------
    # AI Analysis
    # ------------------------------
    st.header("🤖 AI Candidate Analysis")

    st.write(summary)

    st.divider()

    st.success("Resume Analysis Completed Successfully!")