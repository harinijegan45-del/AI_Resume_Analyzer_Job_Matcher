# AI Resume Analyzer & Job Matcher

A Python web application prototype that extracts resume text, detects selected skills, and ranks sample job roles using TF-IDF and cosine similarity.

## Technologies
- Python — application logic
- Streamlit — web interface
- Pandas — loads and manages job data
- NumPy — numerical score handling
- Scikit-learn — TF-IDF and cosine similarity
- pypdf and python-docx — PDF and DOCX text extraction

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Start the app: `streamlit run app.py`
5. Open the local URL printed in the terminal (usually http://localhost:8501).

## Deploy on Streamlit Community Cloud
1. Sign in at https://share.streamlit.io/ using GitHub.
2. Choose this repository.
3. Select branch `main` and main file `app.py`.
4. Click Deploy.

## Dataset
`jobs.csv` is a small illustrative dataset created for this demonstration. Replace it with a larger, reviewed dataset for a more meaningful evaluation.

## Limitations
This is an educational prototype. Skill extraction uses a small keyword list, and the match score is text similarity—not a probability of being hired or an automated hiring decision. Avoid uploading confidential personal information to untrusted deployments.
