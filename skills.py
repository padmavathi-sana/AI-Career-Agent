SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "numpy",
    "pandas",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "git",
    "docker",
    "aws",
    "azure",
    "gcp",
    "nlp",
    "computer vision",
    "mlops",
    "powerbi",
    "tableau",
    "rest api",
    "feature engineering",
    "data analysis",
    "react"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill.lower() in text:

            found.append(skill)

    return found


def skill_gap(
    resume_skills,
    job_skills
):

    return list(
        set(job_skills)
        - set(resume_skills)
    )