# 📄 AI Resume Screening Agent

An AI-powered Applicant Tracking System (ATS) that automatically evaluates resumes against a job description using Semantic Similarity and Large Language Models (LLMs). The application helps recruiters quickly identify the most suitable candidates by analyzing resumes, calculating ATS scores, and generating AI-powered recommendations.

---

# 🚀 Features

- 📄 Upload a Job Description (.txt)
- 📂 Upload Multiple Resume PDFs
- 👤 Automatically Extract Candidate Information (Name, Email, Phone Number)
- 🧠 Semantic Similarity Matching using Sentence Transformers
- 🤖 AI Resume Analysis using Groq LLM
- ⭐ Generate ATS Match Score
- 📊 Candidate Ranking Dashboard
- ✅ AI Recommendation (Shortlist / Further Review / Reject)
- 💪 Identify Candidate Strengths
- ❌ Detect Missing Skills
- 📥 Download Results as CSV
- 🌐 Interactive Streamlit Web Dashboard

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Sentence Transformers
- Scikit-learn
- Pandas
- PDFPlumber
- Python Dotenv

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/rajesh580/AI-Resume-Screening-Agent.git
cd AI-Resume-Screening-Agent
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run src/streamlit_app.py
```

The application will open automatically in your browser.

---

# 📂 Project Structure

```text
resume-screening-agent/
│
├── src/
│   ├── streamlit_app.py
│   ├── app.py
│   ├── parser.py
│   ├── resume_parser.py
│   ├── similarity.py
│   ├── llm.py
│   └── utils.py
│
├── data/
│   └── job_description.txt
│
├── resumes/
│   └── sample_resumes.pdf
│
├── output/
│   └── resume_screening_results.csv
│
├── requirements.txt
├── README.md
├── .env.example
└── screenshots/
```

---

# 📥 Sample Input

### Job Description

```
Python Backend Developer

Required Skills

Python
FastAPI
REST APIs
SQL
Git
Docker

Preferred Skills

AWS
Kubernetes
```

### Resume

Upload one or more PDF resumes through the Streamlit dashboard.

---

# 📤 Sample Output

The application provides:

- Candidate Information
- Semantic Similarity Score
- AI Match Score
- Final ATS Score
- Candidate Strengths
- Missing Skills
- AI Recommendation
- Candidate Ranking
- Downloadable CSV Report

---

# ⚖️ Tradeoffs

### Design Decisions

- Sentence Transformers were used for semantic similarity because they provide fast and accurate text embeddings.
- Groq Llama was selected for AI resume evaluation due to its speed and high-quality responses.
- Candidate information is extracted using regular expressions to keep the application lightweight.

### Limitations

- Supports PDF resumes only.
- Does not support scanned/image-based resumes (OCR).
- No recruiter authentication.
- No database integration.

### Future Improvements

- OCR Support for scanned resumes
- DOCX Resume Support
- Recruiter Login & Dashboard
- Email Notifications
- Resume History
- Database Storage
- Cloud Deployment

---
## Scoring Method

The Resume Screening Agent evaluates candidates using three components:

1. **Semantic Similarity (60%)**
   - Sentence Transformers are used to compare the resume with the job description.
   - This measures how semantically similar the candidate's experience and skills are to the job requirements.

2. **LLM Match Score (40%)**
   - Groq Llama analyzes the resume against the job description.
   - It generates:
     - Match Score
     - Recommendation
     - Strengths
     - Missing Skills
     - Summary

### Final ATS Score

Final ATS Score =

0.6 × Semantic Similarity

+

0.4 × LLM Match Score

Candidates are ranked in descending order of the Final ATS Score.
---
# 📸 Screenshots

- Home Page
- Resume Upload
- Resume Analysis
- Candidate Ranking
- CSV Export

---

# 📋 Deliverables

This project includes:

- ✅ Resume Parsing
- ✅ Candidate Information Extraction
- ✅ Semantic Similarity Matching
- ✅ AI Resume Analysis
- ✅ ATS Score Generation
- ✅ Candidate Ranking
- ✅ CSV Export
- ✅ Interactive Streamlit Dashboard

---

# 👨‍💻 Author

**Rajesh Rajoli**

GitHub: https://github.com/rajesh580

---

## ⭐ If you found this project useful, consider giving it a star!