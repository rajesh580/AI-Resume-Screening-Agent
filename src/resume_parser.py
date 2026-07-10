import re


def extract_candidate_details(resume_text):

    # -------------------------
    # Email
    # -------------------------

    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        resume_text
    )

    email = email_match.group(0) if email_match else "Not Found"

    # -------------------------
    # Phone Number
    # -------------------------

    phone_match = re.search(
        r'(\+?\d[\d\s\-]{8,}\d)',
        resume_text
    )

    phone = phone_match.group(0) if phone_match else "Not Found"

    # -------------------------
    # Candidate Name
    # -------------------------

    lines = resume_text.split("\n")

    name = "Not Found"

    for line in lines[:5]:

        line = line.strip()

        if len(line.split()) >= 2 and len(line) < 40:

            name = line

            break

    return {
        "name": name,
        "email": email,
        "phone": phone
    }