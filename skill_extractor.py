import re
import ollama

# Predefined technical skills database
SKILLS_DB = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "pandas",
    "numpy",
    "power bi",
    "excel",
    "java",
    "c++",
    "dbms",
    "streamlit",
    "tensorflow",
    "deep learning",
    "flask"
]


def extract_skills_db(text):
    """
    Extract skills from resume text using regex
    """
    
    # Convert resume text to lowercase
    text = text.lower()

    # Store matched skills
    extracted_skills = []

    # Check each skill
    for skill in SKILLS_DB:

        # Create regex pattern for exact skill match
        pattern = r"\b" + re.escape(skill) + r"\b"

        # Search skill in resume text
        if re.search(pattern, text):
            extracted_skills.append(skill.title())

    return extracted_skills






