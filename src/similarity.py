from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(job_description, resume_text):
    """
    Calculate semantic similarity between
    a job description and a resume.

    Returns:
        float (percentage)
    """

    # Convert text to embeddings
    jd_embedding = model.encode([job_description])
    resume_embedding = model.encode([resume_text])

    # Calculate cosine similarity
    similarity = cosine_similarity(jd_embedding, resume_embedding)[0][0]

    # Convert to percentage
    return round(similarity * 100, 2)