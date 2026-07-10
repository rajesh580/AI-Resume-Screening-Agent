# 📄 AI Resume Screening Agent

## 📖 Overview

An AI-powered Applicant Tracking System (ATS) that evaluates resumes against a job description using semantic similarity and a Large Language Model.

## ✨ Features

- **Upload Job Description:** Easily input text-based job descriptions.
- **Upload Multiple Resumes:** Process multiple PDF resumes simultaneously.
- **Resume Parsing & Extraction:** Automatically extract key candidate information (Name, Email, Phone).
- **Semantic Similarity:** Calculate how closely the resume matches the job description.
- **AI Resume Analysis:** Leverage LLMs to identify strengths, missing skills, and generate summaries.
- **ATS Score & Ranking:** Generate a final ATS score and rank candidates from best to worst.
- **CSV Export:** Download a detailed summary report of all processed candidates.
- **Streamlit Dashboard:** A clean, interactive user interface.

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Frontend framework)
- **Groq** (LLM integration)
- **Sentence Transformers** (Semantic similarity)
- **Pandas** (Data manipulation)
- **PDFPlumber** (PDF parsing)

## 🚀 Getting Started

### 1. Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/rajesh580/AI-Resume-Screening-Agent
cd resume-screening-agent
pip install -r requirements.txt
```

### 2. Environment Setup

Create a `.env` file in the root directory and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Application

Launch the Streamlit dashboard:

```bash
streamlit run src/streamlit_app.py
```

## 📂 Project Structure

```text
resume-screening-agent/
├── src/
│   ├── streamlit_app.py       # Main application file
│   ├── parser.py              # PDF extraction logic
│   ├── similarity.py          # Semantic similarity calculations
│   ├── llm.py                 # Groq LLM integration
│   └── resume_parser.py       # Candidate detail extraction
├── .env                       # Environment variables (do not commit)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🔮 Future Improvements

- **OCR Support:** To read text from image-based or scanned PDFs.
- **DOCX Support:** Allow users to upload Word documents.
- **Authentication:** Secure the dashboard with user login.
- **Recruiter Dashboard:** Advanced analytics and historical data tracking.
- **Email Notifications:** Automatically email shortlisted candidates.

## 👨‍💻 Author

**Rajesh Rajoli**

---
---

### 📝 Reviewer / Submission Notes

*(You can keep this section separate from your actual `README.md` or use it as a final checklist before submitting your project).*

#### 11. Demo Resumes
Include **3–4 sample resumes** that you are allowed to share (or create anonymized sample resumes) in a `data/` or `samples/` folder so reviewers can immediately test the project without having to hunt for their own files.
