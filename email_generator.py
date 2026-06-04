def generate_email(score, missing_skills):

    skills_text = ", ".join(missing_skills)

    if not skills_text:
        skills_text = "No major skill gaps detected"

    return f"""
Subject: Application for AI/ML Position

Dear Hiring Manager,

I am excited to apply for the Artificial Intelligence / Machine Learning position.

Based on an analysis of my profile against the job requirements, my current match score is {score:.2f}%.

My background includes Artificial Intelligence, Python, Data Analysis, and AI project development.

Skills I am currently strengthening:
{skills_text}

I am eager to contribute to innovative AI solutions while continuing to expand my technical expertise in machine learning, data science, and cloud technologies.

Thank you for your consideration.

Best Regards,
Padmavathi Sana
"""