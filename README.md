# 📄 AI Resume Screening Agent

An AI-powered Applicant Tracking System (ATS) that automatically evaluates resumes against a job description using **Semantic Similarity** and **Large Language Models (LLMs)**. The application helps recruiters quickly identify the most suitable candidates by analyzing resumes, calculating ATS scores, generating AI-powered recommendations, and ranking candidates based on their relevance to the job description.

---

# 🚀 Features

- 📄 Upload a Job Description (.txt)
- 📂 Upload and Screen Multiple PDF Resumes
- 👤 Automatically Extract Candidate Information (Name, Email, Phone Number)
- 🧠 Semantic Similarity Matching using Sentence Transformers
- 🤖 AI Resume Analysis using Groq LLM
- ⭐ Generate ATS Match Score
- 📊 Generate Final ATS Score
- 🏆 Candidate Ranking Dashboard
- ✅ AI Recommendation (Shortlist / Further Review / Reject)
- 💪 Identify Candidate Strengths
- ❌ Detect Missing Skills
- 📥 Download Ranked Results as CSV
- 🌐 Interactive Streamlit Dashboard

---

# 📄 Supported Resume Format

| Format | Status |
|---------|--------|
| PDF | ✅ Supported |
| DOCX | 🚧 Planned |
| TXT | 🚧 Planned |

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

Create a virtual environment.

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

Install the required dependencies.

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

The Streamlit dashboard will automatically open in your browser.

---

# 🏗️ Architecture

```text
                Job Description
                       │
                       ▼
               Upload Resume PDFs
                       │
                       ▼
               Resume Text Parsing
                       │
                       ▼
        Candidate Information Extraction
                       │
                       ▼
         Semantic Similarity Calculation
                       │
                       ▼
              Groq LLM Resume Analysis
                       │
                       ▼
              Final ATS Score Calculation
                       │
                       ▼
             Candidate Ranking Dashboard
                       │
                       ▼
               Export Results to CSV
```

---

# 📂 Project Structure

```text
resume-screening-agent/
│
├── src/
│   ├── streamlit_app.py
│   ├── app.py
│   ├── parser.py
│   ├── similarity.py
│   ├── llm.py
│   ├── resume_parser.py
│   └── utils.py
│
├── data/
│   └── job_description.txt
│
├── resumes/
│   ├── Rajesh_resume.pdf
│   ├── Priya_resume.pdf
│   ├── Praveen_resume.pdf
│   └── Revanasidd_resume.pdf
│
├── output/
│   └── resume_screening_results.csv
│
├── screenshots/
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# 📥 Sample Input

### Job Description

```text
Python Backend Developer

Required Skills

- Python
- FastAPI
- REST APIs
- SQL
- Git
- Docker

Preferred Skills

- AWS
- Kubernetes
```

### Resume Input

Upload one or more PDF resumes through the Streamlit dashboard.

---

# 📤 Sample Output

The application generates:

- Candidate Information
- Semantic Similarity Score
- LLM Match Score
- Final ATS Score
- AI Recommendation
- Candidate Strengths
- Missing Skills
- Candidate Ranking
- Downloadable CSV Report

---

# ⚖️ Scoring Method

The Resume Screening Agent evaluates candidates using two scoring components.

### 1. Semantic Similarity (60%)

Sentence Transformers generate embeddings for both the resume and the job description. Cosine similarity is then used to measure how closely the resume matches the job description.

### 2. LLM Match Score (40%)

Groq Llama analyzes the resume and provides:

- Match Score
- Recommendation
- Candidate Strengths
- Missing Skills
- Summary

### Final ATS Score

```
Final ATS Score =
(0.6 × Semantic Similarity)
+
(0.4 × LLM Match Score)
```

Candidates are ranked in descending order based on the Final ATS Score.

---

# 📁 Output Files

The application generates:

- 📊 Ranked Candidate Dashboard
- 📄 AI Resume Analysis
- 📥 resume_screening_results.csv

---

# ⚖️ Tradeoffs

## Design Decisions

- Sentence Transformers were selected for semantic similarity because they provide fast and accurate semantic matching.
- Groq Llama is used for qualitative resume evaluation and reasoning.
- Candidate information is extracted using lightweight regular-expression parsing to keep the application simple and efficient.

## Limitations

- Currently supports PDF resumes only.
- DOCX and TXT support are planned for future releases.
- OCR is not implemented for scanned/image-based resumes.
- No recruiter authentication.
- No database integration.

## Future Improvements

- DOCX Resume Support
- TXT Resume Support
- OCR Support for Scanned Resumes
- Recruiter Authentication
- Candidate Database
- Email Notifications
- Resume History
- Cloud Deployment
- Skill Gap Analysis

---

# 📸 Screenshots

Add screenshots of the following pages after running the application.

- Home Page
- Resume Upload
- Resume Analysis
- Candidate Ranking Dashboard
- CSV Export

---

# 📋 Agent Deliverables

This project satisfies the following deliverables:

- ✅ Parse PDF resumes
- ✅ Extract Candidate Information
- ✅ Compute Semantic Similarity
- ✅ AI-powered Resume Evaluation
- ✅ Generate ATS Scores
- ✅ Rank Multiple Candidates
- ✅ Provide AI Reasoning
- ✅ Export Ranked Results as CSV
- ✅ Interactive Streamlit Dashboard

---

# 🙏 Acknowledgements

This project makes use of the following open-source technologies:

- Groq API
- Streamlit
- Sentence Transformers
- Hugging Face
- PDFPlumber
- Pandas
- Scikit-learn

---

# 👨‍💻 Author

**Rajesh Rajoli**

GitHub: https://github.com/rajesh580

---

# 📄 License

This project was developed for educational and hackathon purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.