import os
import tempfile
import pandas as pd
import streamlit as st

from parser import extract_text_from_pdf
from similarity import calculate_similarity
from llm import analyze_resume
from resume_parser import extract_candidate_details


st.title("🤖 AI Resume Screening Agent")

st.caption(
    "AI Powered Applicant Tracking System using Groq + Sentence Transformers"
)

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("📄 AI Resume Screening Agent")

st.markdown("""
### AI Powered Applicant Tracking System

This application screens resumes using:

- 🤖 Groq LLM
- 🧠 Sentence Transformers
- 📄 PDF Resume Parsing
- ⭐ ATS Score
- 🏆 Candidate Ranking
""")

st.divider()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:
    st.header("📋 Instructions")

    st.info(
        """
1. Upload Job Description (.txt)

2. Upload Resume PDFs

3. Click Analyze

4. Download CSV Report
"""
    )

    st.divider()
    st.success("Hackathon Version 1.0")


# -------------------------------------------------------
# Upload Section
# -------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    job_description = st.file_uploader(
        "📄 Upload Job Description",
        type=["txt"]
    )

with col2:
    resume_files = st.file_uploader(
        "📂 Upload Resume PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )


analyze = st.button(
    "🚀 Analyze Resumes",
    use_container_width=True
)


# -------------------------------------------------------
# Helper Function
# -------------------------------------------------------

def save_uploaded_pdf(uploaded_file):
    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )
    temp.write(uploaded_file.getbuffer())
    temp.close()
    return temp.name


# -------------------------------------------------------
# Validation & Execution
# -------------------------------------------------------

if analyze:
    if job_description is None:
        st.error("Please upload a Job Description.")
        st.stop()

    if not resume_files:
        st.error("Please upload at least one Resume.")
        st.stop()

    # Read Job Description
    job_description_text = (
        job_description.read()
        .decode("utf-8")
    )

    st.success("✅ Job Description Loaded Successfully")
    st.divider()
    st.header("📊 Resume Analysis")

    results = []
    progress = st.progress(0)
    total = len(resume_files)

    # Resume processing starts here...
    for i, uploaded_resume in enumerate(resume_files):
        progress.progress((i + 1) / total)
        st.divider()
        st.subheader(f"📄 {uploaded_resume.name}")

        # -------------------------------
        # Save Uploaded Resume
        # -------------------------------
        temp_pdf_path = save_uploaded_pdf(uploaded_resume)

        try:
            # -------------------------------
            # Extract Resume Text
            # -------------------------------
            resume_text = extract_text_from_pdf(temp_pdf_path)

            # -------------------------------
            # Candidate Details
            # -------------------------------
            candidate = extract_candidate_details(resume_text)

            info_col1, info_col2, info_col3 = st.columns(3)

            with info_col1:
                st.metric("👤 Name", candidate["name"])
            with info_col2:
                st.metric("📧 Email", candidate["email"])
            with info_col3:
                st.metric("📞 Phone", candidate["phone"])

            st.divider()

            # -------------------------------
            # Semantic Similarity
            # -------------------------------
            similarity = calculate_similarity(
                job_description_text,
                resume_text
            )
            similarity = round(similarity, 2)
            # -------------------------------
            # AI Analysis
            # -------------------------------
            with st.spinner(f"Analyzing {uploaded_resume.name}..."):
                analysis = analyze_resume(
                    job_description_text,
                    resume_text
                )

            # -------------------------------
            # Final ATS Score
            # -------------------------------
            final_score = round(
                (similarity * 0.6) +
                (analysis["match_score"] * 0.4),
                2
            )
            final_score = round(final_score, 2)

            score_col1, score_col2, score_col3 = st.columns(3)

            with score_col1:
                st.metric(
                    "Semantic Similarity",
                    f"{similarity:.2f}%"
                )
            with score_col2:
                st.metric(
                    "LLM Match Score",
                    f"{analysis['match_score']}%"
                )
            with score_col3:
                st.metric(
                    "⭐ Final ATS Score",
                    f"{final_score}%"
                )

            st.divider()

            # -------------------------------
            # Recommendation
            # -------------------------------
            if analysis["recommendation"].lower() == "shortlist":
                st.success(f"✅ Recommendation: {analysis['recommendation']}")
            else:
                st.error(f"❌ Recommendation: {analysis['recommendation']}")

            # -------------------------------
            # Summary
            # -------------------------------
            st.markdown("### 📝 Summary")
            st.info(analysis["summary"])

            # -------------------------------
            # Strengths
            # -------------------------------
            left, right = st.columns(2)

            with left:
                st.markdown("### ✅ Strengths")
                for skill in analysis["strengths"]:
                    st.success(skill)

            # -------------------------------
            # Missing Skills
            # -------------------------------
            with right:
                st.markdown("### ❌ Missing Skills")
                for skill in analysis["missing_skills"]:
                    st.error(skill)

            # -------------------------------
            # Save Result
            # -------------------------------
            results.append({
                "Name": candidate["name"],
                "Email": candidate["email"],
                "Phone": candidate["phone"],
                "Candidate": uploaded_resume.name,
                "Similarity Score": similarity,
                "LLM Match Score": analysis["match_score"],
                "Final ATS Score": final_score,
                "Recommendation": analysis["recommendation"],
                "Strengths": ", ".join(analysis["strengths"]),
                "Missing Skills": ", ".join(analysis["missing_skills"]),
                "Summary": analysis["summary"]
            })

        except Exception as e:
            st.error(f"Error processing {uploaded_resume.name}")
            st.exception(e)

        finally:
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)

    # Analysis Complete
    # ==========================================
    progress.empty()
    st.divider()
    st.header("🏆 Candidate Ranking")

    # Create DataFrame
    df = pd.DataFrame(results)

    # Sort by Final ATS Score
    if not df.empty:
        df = df.sort_values(
            by="Final ATS Score",
            ascending=False
        )
        df.reset_index(drop=True, inplace=True)
        df.index = df.index + 1

        # -------------------------------
        # Best Candidate
        # -------------------------------
        best = df.iloc[0]

        st.success(
            f"""
🥇 **Best Candidate**

**Name:** {best['Name']}

**Resume:** {best['Candidate']}

**Final ATS Score:** {best['Final ATS Score']}%

**Recommendation:** {best['Recommendation']}
"""
        )

        # -------------------------------
        # Ranking Table
        # -------------------------------
        st.dataframe(
            df[
                [
                    "Name",
                    "Candidate",
                    "Similarity Score",
                    "LLM Match Score",
                    "Final ATS Score",
                    "Recommendation"
                ]
            ],
            use_container_width=True,
            height=350
        )

        # -------------------------------
        # Score Chart
        # -------------------------------
        st.subheader("📊 Candidate Comparison")
        chart_df = df.set_index("Name")[["Final ATS Score"]]
        st.bar_chart(chart_df)

        # -------------------------------
        # Pie Chart Data
        # -------------------------------
        st.subheader("📈 Recommendation Summary")
        recommendation_counts = df["Recommendation"].value_counts()
        st.dataframe(
            recommendation_counts,
            use_container_width=True
        )

        # -------------------------------
        # Download CSV
        # -------------------------------
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Results CSV",
            data=csv,
            file_name="resume_screening_results.csv",
            mime="text/csv",
            use_container_width=True
        )

        # -------------------------------
        # Project Statistics
        # -------------------------------
        st.divider()
        st.header("📌 Statistics")

        stat1, stat2, stat3 = st.columns(3)

        stat1.metric(
            "Total Candidates",
            len(df)
        )

        shortlisted = len(
            df[df["Recommendation"].str.lower() == "shortlist"]
        )

        stat2.metric(
            "Shortlisted",
            shortlisted
        )

        stat3.metric(
            "Rejected",
            len(df) - shortlisted
        )

    else:
        st.warning("No valid results to display. Please check the resume files and try again.")

    # -------------------------------
    # Footer
    # -------------------------------
    st.divider()
    st.caption(
        "Built using Streamlit • Groq • Sentence Transformers • pdfplumber"
    )
    st.balloons()