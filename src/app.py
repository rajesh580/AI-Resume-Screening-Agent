import os
import pandas as pd

from parser import extract_text_from_pdf
from utils import load_job_description
from similarity import calculate_similarity
from llm import analyze_resume
import streamlit as st

def main():

    print("=" * 70)
    st.title("AI Resume Screening Agent")
    print("=" * 70)

    # Load Job Description
    job_description = load_job_description("data/job_description.txt")

    resume_folder = "resumes"

    results = []

    # Analyze each resume
    for file in os.listdir(resume_folder):

        if file.endswith(".pdf"):

            resume_path = os.path.join(resume_folder, file)

            resume = extract_text_from_pdf(resume_path)

            similarity = calculate_similarity(
                job_description,
                resume
            )

            analysis = analyze_resume(
                job_description,
                resume
            )

            results.append({
                "candidate": file,
                "score": similarity,
                "analysis": analysis,
                "resume_text": resume
            })

    # Sort by similarity score
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("\n")
    print("=" * 70)
    print("Candidate Ranking")
    print("=" * 70)

    # Display results
    for index, result in enumerate(results, start=1):

        print(f"\nRank #{index}")
        print(f"Candidate : {result['candidate']}")
        print(f"Similarity: {result['score']}%")
        print("\nAI Analysis")
        print(result["analysis"])
        print("-" * 70)

    # ---------------- CSV Export ----------------

    csv_data = []

    for index, result in enumerate(results, start=1):

        csv_data.append({
            "Rank": index,
            "Candidate": result["candidate"],
            "Similarity Score": result["score"],
            "Recommendation": "See AI Analysis"
        })

    df = pd.DataFrame(csv_data)

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/results.csv", index=False)

    print("\nResults saved to output/results.csv")


if __name__ == "__main__":
    main()