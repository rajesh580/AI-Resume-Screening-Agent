import os

def load_job_description(file_path):
    """
    Read the job description from a text file.
    """

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, file_path)

    with open(full_path, "r", encoding="utf-8") as file:
        return file.read()