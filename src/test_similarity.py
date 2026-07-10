from parser import extract_text_from_pdf
from utils import load_job_description
from similarity import calculate_similarity

# Load the Job Description
job_description = load_job_description("data/job_description.txt")

# Load the Resume
resume = extract_text_from_pdf("resumes/res.pdf")

# Calculate Similarity
score = calculate_similarity(job_description, resume)

print(f"Similarity Score: {score}%")