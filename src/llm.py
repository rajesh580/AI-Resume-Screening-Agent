import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(job_description, resume_text):

    prompt = f"""
You are an experienced HR Recruiter.

Compare the Resume against the Job Description.

Return ONLY valid JSON.

Example:

{{
    "match_score": 85,
    "recommendation": "Shortlist",
    "strengths": [
        "Python",
        "FastAPI",
        "SQL"
    ],
    "missing_skills": [
        "AWS",
        "Docker"
    ],
    "summary": "Candidate has strong backend development skills and is a good fit for the role."
}}

Do not return markdown.

Do not use ```json.

Return only JSON.

Job Description:

{job_description}

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown if present
    content = (
        content.replace("```json", "")
               .replace("```", "")
               .strip()
    )

    try:
        return json.loads(content)

    except Exception:

        # Fallback in case the model doesn't return valid JSON
        return {
            "match_score": 0,
            "recommendation": "Review",
            "strengths": [],
            "missing_skills": [],
            "summary": content
        }