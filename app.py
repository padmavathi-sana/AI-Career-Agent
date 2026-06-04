import streamlit as st
from datetime import date

from modules.resume_parser import extract_text
from modules.matcher import resume_job_score
from modules.email_generator import generate_email
from modules.job_engine import get_jobs
from modules.skills import extract_skills, skill_gap

from modules.tracker import (
    init_db,
    save_application,
    get_data,
    update_status
)

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="AI Career Agent",
    layout="wide"
)

st.title("🚀 AI Career Agent System")

# Initialize Database
init_db()

# --------------------------------
# RESUME ANALYSIS
# --------------------------------

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_desc = st.text_area(
    "Paste Job Description"
)

if resume_file:

    resume_text = extract_text(resume_file)

    st.success("Resume loaded!")

    user_skills = extract_skills(resume_text)

    if job_desc:

        score = resume_job_score(
            resume_text,
            job_desc
        )

        st.subheader("🎯 ATS Match Score")

        st.metric(
            "Match Score",
            f"{score:.2f}%"
        )

        if score >= 80:
            st.success("Excellent Match")
        elif score >= 60:
            st.warning("Moderate Match")
        else:
            st.error("Needs Improvement")

        # -------------------------
        # Skill Gap Analysis
        # -------------------------

        job_skills = extract_skills(job_desc)

        missing = skill_gap(
            user_skills,
            job_skills
        )

        st.subheader("📈 Skill Gap Analysis")

        if len(missing) == 0:

            st.success(
                "Excellent! No major skill gaps found."
            )

        else:

            for skill in missing:

                st.warning(
                    f"Missing Skill: {skill}"
                )

        # -------------------------
        # Email Generation
        # -------------------------

        if st.button("Generate Email"):

            email = generate_email(
                score,
                missing
            )

            st.subheader("📧 AI Email")

            st.text_area(
                "",
                email,
                height=350
            )

# --------------------------------
# JOB RECOMMENDATIONS
# --------------------------------

st.subheader("💼 Job Recommendations")

keyword = st.text_input(
    "Enter Role (e.g. Data Analyst)"
)

if keyword:

    jobs = get_jobs(keyword)

    for job in jobs:

        st.write("✅", job)

# --------------------------------
# APPLICATION TRACKER
# --------------------------------

st.subheader("📝 Track Application")

company = st.text_input(
    "Company Name"
)

role = st.text_input(
    "Role"
)

status = st.selectbox(
    "Status",
    [
        "Applied",
        "Shortlisted",
        "Interview",
        "Rejected",
        "Offer"
    ]
)

if st.button("Save Application"):

    save_application(
        company,
        role,
        status,
        str(date.today())
    )

    st.success(
        "Application Saved!"
    )

# --------------------------------
# UPDATE STATUS
# --------------------------------

st.subheader("✏️ Update Application Status")

df = get_data()

if len(df) > 0:

    selected_company = st.selectbox(
        "Select Company",
        df["company"].unique()
    )

    new_status = st.selectbox(
        "New Status",
        [
            "Applied",
            "Shortlisted",
            "Interview",
            "Rejected",
            "Offer"
        ]
    )

    if st.button("Update Status"):

        update_status(
            selected_company,
            new_status
        )

        st.success(
            f"{selected_company} updated to {new_status}"
        )

        st.rerun()

# --------------------------------
# DASHBOARD
# --------------------------------

st.subheader("📊 Application Dashboard")

df = get_data()

if len(df) > 0:

    st.dataframe(df)

    interviews = len(
        df[df["status"] == "Interview"]
    )

    offers = len(
        df[df["status"] == "Offer"]
    )

    shortlisted = len(
        df[df["status"] == "Shortlisted"]
    )

    rejected = len(
        df[df["status"] == "Rejected"]
    )

    applications = len(df)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Applications",
            applications
        )

    with col2:
        st.metric(
            "Shortlisted",
            shortlisted
        )

    with col3:
        st.metric(
            "Interviews",
            interviews
        )

    with col4:
        st.metric(
            "Offers",
            offers
        )

    with col5:
        st.metric(
            "Rejected",
            rejected
        )

    success_rate = (
        offers / applications
    ) * 100

    st.metric(
        "Success Rate",
        f"{success_rate:.1f}%"
    )

    st.subheader(
        "📈 Status Distribution"
    )

    st.bar_chart(
        df["status"].value_counts()
    )

else:

    st.info(
        "No applications yet"
    )