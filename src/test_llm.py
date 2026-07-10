from parser import extract_text_from_pdf
from utils import load_job_description
from llm import analyze_resume

# Load Job Description
job_description = load_job_description("data/job_description.txt")

# Load Resume
resume = extract_text_from_pdf("resumes/res.pdf")

# Analyze Resume
result = analyze_resume(job_description, resume)

print(result)