# Project Report: AI Resume Analyzer & Job Matcher

## Abstract
This Python application accepts a resume in PDF, DOCX, or TXT format, extracts readable text, identifies selected skills, and compares the resume with sample job descriptions stored in a CSV file. It ranks roles using TF-IDF features and cosine similarity.

## Objectives
- Accept a resume file.
- Extract and clean its text.
- Identify skills from a predefined keyword list.
- Compare resume text with job descriptions.
- Display ranked job roles and an estimated similarity score.

## Technologies
| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web interface |
| Pandas | Read and manage CSV job data |
| NumPy | Handle and round numerical scores |
| Scikit-learn | TF-IDF and cosine similarity |
| pypdf / python-docx | Read PDF and DOCX files |

## Workflow
1. User uploads a resume.
2. The app extracts text.
3. Text is cleaned.
4. Skill keywords are identified.
5. TF-IDF converts resume and job text into vectors.
6. Cosine similarity compares the vectors.
7. Roles are sorted by score and displayed.

## Concepts
**TF-IDF** represents text numerically and gives greater weight to terms that are informative within a document collection.

**Cosine similarity** measures the similarity between two vectors. A higher score means the resume text is more similar to the job description.

The displayed score is an estimated text-similarity score, not a hiring probability.

## Expected Output
- Resume upload confirmation
- Extracted resume text
- Detected skills
- Ranked job-role table
- Best matching role and estimated score

## Run Instructions
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Simple Presentation
Good morning everyone. My project title is AI Resume Analyzer and Job Matcher. I developed this application using Python. The user uploads a resume, and the application extracts the text and identifies skills. Then it compares the resume with sample job descriptions using TF-IDF and cosine similarity. Pandas is used to manage job data, NumPy is used for numerical score handling, Scikit-learn is used for text similarity, and Streamlit is used to create the user interface. Finally, the application displays identified skills and ranks suitable job roles based on the estimated matching score. The purpose is to help job seekers understand which roles are closer to their resume.

## Sample Review Questions
**Why did you choose this topic?** Resume screening is a common recruitment task. This project demonstrates how Python can compare resume content with job requirements.

**What data did you use?** A sample CSV dataset containing job titles, descriptions, and required skills. The uploaded resume is the input data.

**Why Pandas?** To read and manage job information in table form.

**Why NumPy?** To handle numerical similarity scores.

**What is Streamlit?** A Python framework for building interactive web apps.

**What is TF-IDF?** A method to convert text into numerical features based on word importance.

**What is cosine similarity?** A measure of similarity between two text vectors.

**Is the score a hiring probability?** No. It is an educational text-similarity estimate only.

## Limitations and Future Enhancements
The current demo uses a small sample dataset and a predefined keyword list. Future work can add a larger reviewed dataset, improved NLP-based skill extraction, experience and location filters, and privacy-aware storage.

## Conclusion
The project demonstrates an end-to-end Python workflow combining file extraction, text preprocessing, data handling, and text similarity for resume-to-job comparison.
