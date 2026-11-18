import re
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Analyzer & Job Matcher", page_icon="📄", layout="wide")
st.title("AI Resume Analyzer & Job Matcher")
st.write("Upload your resume to identify skills and compare it with sample job roles.")

JOBS_FILE = Path(__file__).parent / "jobs.csv"

@st.cache_data
def load_jobs():
    return pd.read_csv(JOBS_FILE)

def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith(".txt"):
        return uploaded_file.getvalue().decode("utf-8", errors="ignore")
    if name.endswith(".pdf"):
        from pypdf import PdfReader
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if name.endswith(".docx"):
        from docx import Document
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)
    raise ValueError("Upload a PDF, DOCX, or TXT file.")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

SKILLS = [
    "python", "java", "sql", "html", "css", "javascript", "react",
    "bootstrap", "pandas", "numpy", "machine learning", "data analysis",
    "flask", "django", "streamlit", "git", "excel", "power bi",
    "communication", "problem solving"
]

def find_skills(text):
    cleaned = clean_text(text)
    return sorted({
        skill.title() for skill in SKILLS
        if re.search(r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])", cleaned)
    })

def calculate_matches(resume_text, job_data):
    documents = [clean_text(resume_text)] + [
        clean_text(str(row["description"]) + " " + str(row["skills"]))
        for _, row in job_data.iterrows()
    ]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)
    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    results = job_data.copy()
    results["Match Score"] = np.round(scores * 100, 2)
    return results.sort_values("Match Score", ascending=False)

jobs = load_jobs()
with st.sidebar:
    st.header("About")
    st.write("A learning prototype that compares resume text with sample job descriptions.")
    st.caption("Scores are text-similarity estimates, not hiring probabilities.")

uploaded_file = st.file_uploader("Choose your resume", type=["pdf", "docx", "txt"])
if uploaded_file:
    try:
        resume_text = extract_text(uploaded_file)
        if not resume_text.strip():
            st.error("No readable text found. Try a text-based PDF, DOCX, or TXT file.")
            st.stop()

        st.success("Resume uploaded and text extracted.")
        with st.expander("View extracted text"):
            st.write(resume_text[:5000])

        skills = find_skills(resume_text)
        st.subheader("Skills identified")
        st.write(", ".join(skills) if skills else "No skills from the demo keyword list were detected.")

        matches = calculate_matches(resume_text, jobs)
        st.subheader("Recommended job roles")
        st.dataframe(
            matches[["role", "description", "skills", "Match Score"]].rename(
                columns={"role": "Job Role", "description": "Job Description", "skills": "Required Skills"}
            ),
            use_container_width=True,
            hide_index=True
        )
        best = matches.iloc[0]
        left, right = st.columns(2)
        left.metric("Best matching role", best["role"])
        right.metric("Estimated match score", f'{best["Match Score"]:.2f}%')
        st.info("Use this result as guidance. Add only skills and experience you genuinely have.")
    except Exception as error:
        st.error(f"Unable to analyze this file: {error}")
else:
    st.info("Upload a resume to begin.")
    st.subheader("Sample job roles")
    st.dataframe(jobs[["role", "skills"]], use_container_width=True, hide_index=True)
