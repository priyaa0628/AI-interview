# app.py

import streamlit as st
from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills_db
from modules.question_generator import generate_questions
from modules.evaluator import evaluate_answers
from streamlit_option_menu import option_menu
import base64              # For video
from modules.aptitude_generator import generate_aptitude_questions      # Aptitude Test
import time



# Performance tracker 



if "technical_score" not in st.session_state:
    st.session_state.technical_score = 0

if "aptitude_score" not in st.session_state:
    st.session_state.aptitude_score = 0

if "progress_history" not in st.session_state:
    st.session_state.progress_history = []
















# Performance tracker

if "technical_score" not in st.session_state:
    st.session_state.technical_score = 0

if "aptitude_score" not in st.session_state:
    st.session_state.aptitude_score = 0

if "progress_history" not in st.session_state:
    st.session_state.progress_history = []

# NEW OPTIONAL METRICS
if "total_tests" not in st.session_state:
    st.session_state.total_tests = 0

if "best_score" not in st.session_state:
    st.session_state.best_score = 0





























































with st.sidebar:
    menu_bar=option_menu(
    menu_title="MENU",
    options=("Home","Resume Vision","Practice Zone","Aptitude Test","Dashboard","HelpBot","AboutUs"),
    icons=( "house","file-earmark-person","laptop","patch-question","bar-chart-line","robot","info-circle"),
    menu_icon="menu-button-wide",
    default_index=0,
    )






if menu_bar == "Home":

    # =========================================================
    # PREMIUM GLOBAL CSS
    # =========================================================

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(180deg,#020617,#0f172a,#111827);
    }

    section[data-testid="stSidebar"]{
        background: linear-gradient(180deg,#020617,#0f172a,#111827);
    }

    .main .block-container{
        padding-top: 2rem;
        max-width: 1300px;
    }

    /* HERO */

    .hero-section{
        position:relative;
        overflow:hidden;
        padding:70px;
        border-radius:35px;
        background:
        radial-gradient(circle at top right, rgba(59,130,246,.35), transparent 30%),
        radial-gradient(circle at bottom left, rgba(168,85,247,.28), transparent 30%),
        linear-gradient(135deg,#0f172a,#1e293b,#111827);

        border:1px solid rgba(255,255,255,.08);
        box-shadow:0 25px 60px rgba(0,0,0,.45);
        margin-bottom:35px;
    }

    .hero-badge{
        display:inline-block;
        background:rgba(255,255,255,.08);
        color:#e2e8f0;
        padding:10px 18px;
        border-radius:999px;
        font-size:14px;
        margin-bottom:20px;
        border:1px solid rgba(255,255,255,.08);
    }

    .hero-title{
        font-size:68px;
        font-weight:900;
        line-height:1.1;
        color:white;
        margin-bottom:15px;
    }

    .hero-subtitle{
        font-size:20px;
        color:#cbd5e1;
        line-height:1.8;
        margin-bottom:25px;
    }

    .hero-btn{
        background:linear-gradient(135deg,#3b82f6,#7c3aed);
        padding:14px 28px;
        border-radius:14px;
        display:inline-block;
        color:white;
        font-weight:700;
        margin-top:10px;
        box-shadow:0 10px 30px rgba(59,130,246,.3);
    }

    /* TOP STATS */

    .top-stats{
        display:grid;
        grid-template-columns:repeat(4,1fr);
        gap:20px;
        margin-top:20px;
        margin-bottom:40px;
    }

    .top-card{
        background:linear-gradient(180deg,#111827,#1f2937);
        padding:28px;
        border-radius:24px;
        text-align:center;
        border:1px solid rgba(255,255,255,.06);
        box-shadow:0 10px 25px rgba(0,0,0,.25);
        transition:.35s;
    }

    .top-card:hover{
        transform:translateY(-8px);
        border:1px solid #3b82f6;
        box-shadow:0 20px 40px rgba(59,130,246,.25);
    }

    .top-number{
        font-size:42px;
        font-weight:800;
        color:white;
    }

    .top-label{
        color:#cbd5e1;
        margin-top:8px;
    }

    /* FEATURE GRID */

    .feature-grid{
        display:grid;
        grid-template-columns:repeat(3,1fr);
        gap:24px;
        margin-top:25px;
        margin-bottom:40px;
    }

    .feature-box{
        background:linear-gradient(180deg,#111827,#1f2937);
        padding:32px;
        border-radius:26px;
        border:1px solid rgba(255,255,255,.08);
        transition:.35s;
        box-shadow:0 10px 30px rgba(0,0,0,.25);
    }

    .feature-box:hover{
        transform:translateY(-10px);
        border:1px solid #3b82f6;
        box-shadow:0 25px 50px rgba(59,130,246,.25);
    }

    .feature-icon{
        font-size:48px;
        margin-bottom:15px;
    }

    .feature-title{
        font-size:24px;
        font-weight:700;
        color:white;
        margin-bottom:12px;
    }

    .feature-desc{
        color:#cbd5e1;
        line-height:1.7;
    }

    /* SECTION TITLE */

    .section-title{
        color:white;
        font-size:38px;
        font-weight:800;
        margin-top:20px;
        margin-bottom:10px;
    }

    .section-sub{
        color:#cbd5e1;
        margin-bottom:25px;
    }

    /* TIMELINE */

    .timeline-card{
        background:#111827;
        padding:24px;
        border-radius:20px;
        color:white;
        border-left:5px solid #3b82f6;
        margin-bottom:15px;
    }

    /* TESTIMONIAL */

    .testimonial{
        background:#111827;
        padding:28px;
        border-radius:24px;
        color:white;
        border:1px solid rgba(255,255,255,.06);
        height:100%;
    }

    /* TECH STACK */

    .tech-box{
        background:#0f172a;
        padding:45px;
        border-radius:30px;
        border:1px solid rgba(255,255,255,.08);
        margin-top:40px;
        margin-bottom:40px;
    }

    .tech-item{
        color:white;
        font-size:24px;
        font-weight:700;
    }

    /* CTA */

    .cta-box{
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        padding:70px;
        border-radius:35px;
        text-align:center;
        color:white;
        margin-top:50px;
        box-shadow:0 25px 50px rgba(59,130,246,.35);
    }

    </style>
    """, unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

    st.markdown("""
<div class="hero-badge">
    🚀 AI-Powered Career Preparation Platform
</div>

<div class="hero-title">
    Crack Interviews <br> Smarter With AI
</div>

<div class="hero-subtitle">
    Resume Intelligence • Technical Practice • Aptitude Mastery • AI Analytics
</div>

<div class="hero-btn">
    🎯 Start Your Preparation Journey
</div>
""", unsafe_allow_html=True)

    # =========================================================
    # VIDEO HEADER
    # =========================================================

    st.markdown("""
    <div style='
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    padding:45px;
    border-radius:30px;
    margin-bottom:25px;
    text-align:center;
    color:white;
    box-shadow:0 20px 40px rgba(37,99,235,.25);
    '>

    <h1 style='font-size:52px;'>
    🎯 Experience Smart AI Interview Preparation
    </h1>

    <p style='font-size:20px;color:#e2e8f0;'>
    Modern Interview Practice • Resume Analysis • Career Readiness
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # VIDEO SECTION
    # =========================================================

    import base64

    video_path = "assets/video_interview.mp4"

    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>

        .video-container {{
            width:100%;
            border-radius:28px;
            overflow:hidden;
            box-shadow:0 20px 45px rgba(0,0,0,.35);
            margin-bottom:40px;
        }}

        .video-container video {{
            width:100%;
            display:block;
        }}

        </style>

        <div class="video-container">
            <video autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================================================
    # FEATURES
    # =========================================================

    st.markdown("""
    <div class="section-title">
    🔥 AI Platform Features
    </div>

    <div class="section-sub">
    Complete AI-powered ecosystem for interview preparation and placement success.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-grid">

    <div class="feature-box">
    <div class="feature-icon">📄</div>
    <div class="feature-title">Resume Vision</div>
    <div class="feature-desc">
    AI-powered ATS analysis with intelligent improvement suggestions and profile enhancement.
    </div>
    </div>

    <div class="feature-box">
    <div class="feature-icon">💻</div>
    <div class="feature-title">Practice Zone</div>
    <div class="feature-desc">
    Generate personalized technical interview questions based on extracted skills.
    </div>
    </div>

    <div class="feature-box">
    <div class="feature-icon">🧠</div>
    <div class="feature-title">Aptitude Training</div>
    <div class="feature-desc">
    Practice quantitative aptitude and logical reasoning for placement preparation.
    </div>
    </div>

    <div class="feature-box">
    <div class="feature-icon">📊</div>
    <div class="feature-title">Analytics Dashboard</div>
    <div class="feature-desc">
    Track technical performance and identify strengths and weaknesses.
    </div>
    </div>

    <div class="feature-box">
    <div class="feature-icon">🤖</div>
    <div class="feature-title">AI HelpBot</div>
    <div class="feature-desc">
    Career guidance, coding help, interview support, and smart doubt solving.
    </div>
    </div>

    <div class="feature-box">
    <div class="feature-icon">⚡</div>
    <div class="feature-title">Local AI Engine</div>
    <div class="feature-desc">
    Powered by Ollama + Llama models for fast and private AI inference.
    </div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # HOW IT WORKS
    # =========================================================

    st.markdown("""
    <div class="section-title">
    ⚙ How It Works
    </div>

    <div class="section-sub">
    Smart AI-driven interview preparation workflow.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="timeline-card">
        <h3>1️⃣ Upload Resume</h3>
        <p>Upload your PDF resume for analysis.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="timeline-card">
        <h3>2️⃣ Extract Skills</h3>
        <p>AI detects technologies and career strengths.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="timeline-card">
        <h3>3️⃣ Practice Questions</h3>
        <p>Attempt personalized technical and aptitude tests.</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="timeline-card">
        <h3>4️⃣ Track Progress</h3>
        <p>Analyze readiness using performance dashboard.</p>
        </div>
        """, unsafe_allow_html=True)

    # =========================================================
    # TESTIMONIALS
    # =========================================================

    st.markdown("""
    <div class="section-title">
    🌟 Success Stories
    </div>
    """, unsafe_allow_html=True)

    t1, t2, t3 = st.columns(3)

    with t1:
        st.markdown("""
        <div class="testimonial">
        <h3>👨‍🎓 Aman</h3>
        <p>
        “The Resume Analyzer improved my ATS score and helped me prepare better.”
        </p>
        </div>
        """, unsafe_allow_html=True)

    with t2:
        st.markdown("""
        <div class="testimonial">
        <h3>👩‍💻 Priya</h3>
        <p>
        “Practice Zone gave me confidence for technical interviews.”
        </p>
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.markdown("""
        <div class="testimonial">
        <h3>🧠 Rahul</h3>
        <p>
        “Aptitude training improved my placement preparation significantly.”
        </p>
        </div>
        """, unsafe_allow_html=True)

    # =========================================================
    # TECH STACK
    # =========================================================

    st.markdown("""
    <div class="tech-box">

    <h1 style='text-align:center;color:white;'>
    ⚡ Technology Stack
    </h1>

    <div style='
    display:flex;
    justify-content:space-around;
    flex-wrap:wrap;
    gap:25px;
    margin-top:35px;
    '>

    <div class="tech-item">🐍 Python</div>
    <div class="tech-item">🎈 Streamlit</div>
    <div class="tech-item">🤖 Ollama</div>
    <div class="tech-item">🧠 Llama 3</div>
    <div class="tech-item">📊 Plotly</div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # WHY CHOOSE US
    # =========================================================

    st.markdown("""
    <div class="section-title">
    🚀 Why Choose This Platform?
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns(2)

    with left:
        st.success("✅ AI-Based Personalized Interview Preparation")
        st.success("✅ Resume ATS Intelligence")
        st.success("✅ Technical + Aptitude Training")
        st.success("✅ Beginner Friendly UI")

    with right:
        st.info("🚀 Real-time Performance Tracking")
        st.info("🚀 Smart Analytics Dashboard")
        st.info("🚀 Fast Local AI Inference")
        st.info("🚀 Ideal for Placements & Interviews")

    # =========================================================
    # FINAL CTA
    # =========================================================

    st.markdown("""
    <div class="cta-box">

    <h1 style='font-size:60px;'>
    🚀 Ready To Crack Your Dream Job?
    </h1>

    <p style='
    font-size:22px;
    margin-top:18px;
    color:#e2e8f0;
    '>

    Start your AI-powered interview preparation journey today.

    </p>

    </div>
    """, unsafe_allow_html=True)
    





elif menu_bar=="Resume Vision":

    import plotly.express as px
    import pandas as pd
    import re

    # =========================================================
    # PREMIUM PAGE CONFIG
    # =========================================================

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(180deg,#020617,#0f172a,#111827);
    }

    .main-title{
        font-size:55px;
        font-weight:800;
        color:white;
        margin-bottom:5px;
    }

    .sub-title{
        color:#cbd5e1;
        font-size:18px;
        margin-bottom:35px;
    }

    .premium-card{
        background:linear-gradient(145deg,#111827,#1f2937);
        padding:28px;
        border-radius:24px;
        border:1px solid rgba(255,255,255,0.06);
        box-shadow:0 10px 30px rgba(0,0,0,0.3);
    }

    .metric-box{
        background:linear-gradient(145deg,#111827,#1e293b);
        padding:22px;
        border-radius:22px;
        text-align:center;
        border:1px solid rgba(255,255,255,.06);
    }

    .metric-number{
        font-size:38px;
        font-weight:800;
        color:white;
    }

    .metric-text{
        color:#cbd5e1;
        margin-top:6px;
    }

    .skill-pill{
        display:inline-block;
        padding:10px 18px;
        border-radius:999px;
        margin:6px;
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        color:white;
        font-weight:600;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================================================
    # HERO SECTION
    # =========================================================

    st.markdown(
        """
        <div class="main-title">
            📄 Resume Vision AI
        </div>

        <div class="sub-title">
            AI-Powered ATS Resume Analyzer • Smart Career Insights • Resume Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================================================
    # FILE UPLOAD
    # =========================================================

    uploaded_file = st.file_uploader(
        "Upload Your Resume (PDF Only)",
        type=["pdf"]
    )

    if uploaded_file:

        with st.spinner("Analyzing Resume..."):

            # =========================================================
            # EXTRACT RESUME TEXT
            # =========================================================

            resume_text = extract_text_from_pdf(uploaded_file)

            lower_resume = resume_text.lower()

            # =========================================================
            # DETECT SKILLS
            # =========================================================

            skills_db = [
                "python","java","c","c++","sql","html","css",
                "javascript","react","node","machine learning",
                "data science","streamlit","django","flask",
                "git","github","ai","mongodb"
            ]

            detected_skills = []

            for skill in skills_db:
                if skill.lower() in lower_resume:
                    detected_skills.append(skill)

            # =========================================================
            # ATS SCORE LOGIC
            # =========================================================

            score = 0
            feedback = []
            strengths = []

            # Email
            if "@" in resume_text:
                score += 10
                strengths.append("Professional email added")
            else:
                feedback.append("Add professional email address")

            # LinkedIn
            if "linkedin" in lower_resume:
                score += 10
                strengths.append("LinkedIn profile detected")
            else:
                feedback.append("Add LinkedIn profile")

            # GitHub
            if "github" in lower_resume:
                score += 10
                strengths.append("GitHub portfolio detected")
            else:
                feedback.append("Add GitHub profile")

            # Education
            if "education" in lower_resume:
                score += 15
                strengths.append("Education section available")
            else:
                feedback.append("Add Education section")

            # Projects
            if "project" in lower_resume:
                score += 15
                strengths.append("Projects section looks good")
            else:
                feedback.append("Add Projects section")

            # Experience
            if "experience" in lower_resume or "internship" in lower_resume:
                score += 15
                strengths.append("Experience section available")
            else:
                feedback.append("Add Internship/Experience")

            # Certifications
            if "certification" in lower_resume:
                score += 10
                strengths.append("Certifications detected")
            else:
                feedback.append("Add Certifications")

            # Skills scoring
            if len(detected_skills) >= 8:
                score += 15
            elif len(detected_skills) >= 5:
                score += 10
            elif len(detected_skills) >= 3:
                score += 5
            else:
                feedback.append("Add more technical skills")

        # =========================================================
        # ATS SCORE SECTION
        # =========================================================

        st.subheader("🎯 ATS Resume Score")

        st.progress(score)

        if score >= 80:
            st.success(f"Excellent Resume Score: {score}/100")
        elif score >= 60:
            st.info(f"Good Resume Score: {score}/100")
        else:
            st.error(f"Low Resume Score: {score}/100")

        st.write("")

        # =========================================================
        # METRICS
        # =========================================================

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{len(detected_skills)}</div>
                <div class="metric-text">Skills</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{len(feedback)}</div>
                <div class="metric-text">Suggestions</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            total_words = len(resume_text.split())

            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{total_words}</div>
                <div class="metric-text">Words</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{score}%</div>
                <div class="metric-text">ATS Match</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        # =========================================================
        # SKILLS
        # =========================================================

        st.subheader("💻 Detected Skills")

        if detected_skills:

            skill_html = ""

            for skill in detected_skills:
                skill_html += f"<span class='skill-pill'>{skill.upper()}</span>"

            st.markdown(skill_html, unsafe_allow_html=True)

        else:
            st.warning("No technical skills detected")

        st.write("")
        st.write("")

        # =========================================================
        # SECTION ANALYSIS
        # =========================================================

        st.subheader("📊 Resume Section Analysis")

        section_data = pd.DataFrame({
            "Section": [
                "Education",
                "Projects",
                "Experience",
                "Certifications",
                "LinkedIn",
                "GitHub"
            ],
            "Status": [
                1 if "education" in lower_resume else 0,
                1 if "project" in lower_resume else 0,
                1 if "experience" in lower_resume else 0,
                1 if "certification" in lower_resume else 0,
                1 if "linkedin" in lower_resume else 0,
                1 if "github" in lower_resume else 0,
            ]
        })

        fig = px.bar(
            section_data,
            x="Section",
            y="Status",
            text="Status",
            title="Resume Completeness"
        )

        st.plotly_chart(fig, use_container_width=True)

        # =========================================================
        # STRENGTHS
        # =========================================================

        st.subheader("🚀 Resume Strengths")

        if strengths:
            for item in strengths:
                st.success(item)

        st.write("")
        st.write("")

        # =========================================================
        # IMPROVEMENTS
        # =========================================================

        st.subheader("📌 Improvement Suggestions")

        if feedback:
            for item in feedback:
                st.warning(item)
        else:
            st.success("Your resume looks highly optimized.")

        # =========================================================
        # CAREER READINESS
        # =========================================================

        st.subheader("📈 Career Readiness")

        if score >= 80:
            st.success("🚀 Highly Interview Ready")
        elif score >= 60:
            st.info("📘 Almost Ready For Placements")
        else:
            st.error("⚠️ Resume Needs Improvement")

        # =========================================================
        # AI SUMMARY
        # =========================================================

        st.subheader("🤖 AI Resume Summary")

        st.info(
            f"""
            Resume achieved ATS score of {score}/100.

            Total detected technical skills: {len(detected_skills)}

            Resume appears {'well optimized' if score >= 75 else 'moderately optimized'} 
            for technical jobs and placement interviews.
            """
        )

        # =========================================================
        # DOWNLOAD REPORT
        # =========================================================

        st.subheader("📥 Download Report")

        report = f"""
Resume ATS Score : {score}/100

Detected Skills:
{', '.join(detected_skills)}

Strengths:
{', '.join(strengths)}

Suggestions:
{', '.join(feedback)}
        """

        st.download_button(
            label="⬇ Download Resume Report",
            data=report,
            file_name="resume_report.txt",
            mime="text/plain"
        )

        # =========================================================
        # FULL RESUME
        # =========================================================

        with st.expander("📃 View Full Resume Content"):
            st.write(resume_text)
































elif menu_bar=="Practice Zone": 
    st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp{
    background:
    radial-gradient(circle at top left, rgba(59,130,246,.18), transparent 25%),
    radial-gradient(circle at bottom right, rgba(168,85,247,.18), transparent 25%),
    linear-gradient(180deg,#020617,#0f172a,#111827);
    overflow-x:hidden;
}

/* PARTICLES */

.particles{
    position:fixed;
    width:100%;
    height:100%;
    top:0;
    left:0;
    z-index:-1;
    overflow:hidden;
}

.particles span{
    position:absolute;
    display:block;
    width:6px;
    height:6px;
    background:rgba(255,255,255,.15);
    border-radius:50%;
    animation:float 25s linear infinite;
    bottom:-150px;
}

/* PARTICLE ANIMATION */

@keyframes float{

    0%{
        transform:translateY(0) scale(0);
        opacity:0;
    }

    10%{
        opacity:1;
    }

    100%{
        transform:translateY(-1200px) scale(1);
        opacity:0;
    }
}

/* RANDOM PARTICLES */

.particles span:nth-child(1){
    left:10%;
    animation-duration:18s;
    width:4px;
    height:4px;
}

.particles span:nth-child(2){
    left:20%;
    animation-duration:22s;
}

.particles span:nth-child(3){
    left:30%;
    animation-duration:16s;
    width:8px;
    height:8px;
}

.particles span:nth-child(4){
    left:40%;
    animation-duration:25s;
}

.particles span:nth-child(5){
    left:50%;
    animation-duration:20s;
}

.particles span:nth-child(6){
    left:60%;
    animation-duration:15s;
    width:7px;
    height:7px;
}

.particles span:nth-child(7){
    left:70%;
    animation-duration:26s;
}

.particles span:nth-child(8){
    left:80%;
    animation-duration:19s;
}

.particles span:nth-child(9){
    left:90%;
    animation-duration:24s;
    width:5px;
    height:5px;
}

/* PREMIUM GLASS CARD */

.premium-card{
    background:rgba(17,24,39,.72);
    backdrop-filter: blur(14px);
    border:1px solid rgba(255,255,255,.08);
    border-radius:28px;
    padding:30px;
    box-shadow:0 10px 40px rgba(0,0,0,.35);
    transition:.35s;
}

.premium-card:hover{
    transform:translateY(-8px);
    border:1px solid rgba(59,130,246,.5);
    box-shadow:0 20px 50px rgba(59,130,246,.22);
}

/* METRIC CARD */

.metric-card{
    background:rgba(15,23,42,.78);
    backdrop-filter: blur(12px);
    border-radius:24px;
    padding:24px;
    border:1px solid rgba(255,255,255,.05);
    text-align:center;
    transition:.3s;
}

.metric-card:hover{
    transform:translateY(-6px);
    border:1px solid #3b82f6;
    box-shadow:0 12px 35px rgba(59,130,246,.25);
}

.metric-number{
    font-size:40px;
    font-weight:800;
    color:white;
}

.metric-label{
    color:#cbd5e1;
    margin-top:8px;
}

/* HERO TITLE */

.practice-title{
    font-size:65px;
    font-weight:900;
    background:linear-gradient(90deg,#ffffff,#60a5fa,#c084fc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;
}

/* SUBTITLE */

.practice-sub{
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:35px;
    line-height:1.8;
}

/* SKILL PILLS */

.skill-pill{
    display:inline-block;
    padding:12px 20px;
    margin:6px;
    border-radius:999px;
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    color:white;
    font-weight:700;
    box-shadow:0 8px 20px rgba(37,99,235,.3);
    transition:.3s;
}

.skill-pill:hover{
    transform:scale(1.08);
}

/* CUSTOM BUTTON */

.stButton>button{
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    color:white;
    border:none;
    padding:14px 28px;
    border-radius:14px;
    font-weight:700;
    transition:.3s;
    box-shadow:0 10px 25px rgba(37,99,235,.25);
}

.stButton>button:hover{
    transform:translateY(-3px);
    box-shadow:0 18px 35px rgba(37,99,235,.35);
}

/* INPUTS */

.stSelectbox div[data-baseweb="select"],
.stSlider{
    background:rgba(17,24,39,.75);
    border-radius:14px;
}

/* RADIO OPTIONS */

div[role="radiogroup"]{
    background:rgba(17,24,39,.6);
    padding:18px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,.05);
}

/* PROGRESS BAR */

.stProgress > div > div > div > div{
    background:linear-gradient(90deg,#3b82f6,#7c3aed);
}

</style>

<!-- PARTICLES -->

<div class="particles">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
</div>

""", unsafe_allow_html=True)

    import plotly.express as px
    import pandas as pd
    import time

    # =========================================================
    # PREMIUM CSS
    # =========================================================

    st.markdown("""
    <style>

    .practice-title{
        font-size:55px;
        font-weight:800;
        color:white;
        margin-bottom:8px;
    }

    .practice-sub{
        color:#cbd5e1;
        font-size:18px;
        margin-bottom:30px;
    }

    .premium-card{
        background:linear-gradient(145deg,#111827,#1f2937);
        padding:28px;
        border-radius:25px;
        border:1px solid rgba(255,255,255,.06);
        box-shadow:0 10px 30px rgba(0,0,0,.35);
        margin-bottom:25px;
    }

    .metric-card{
        background:linear-gradient(145deg,#0f172a,#1e293b);
        padding:24px;
        border-radius:22px;
        text-align:center;
        border:1px solid rgba(255,255,255,.05);
    }

    .metric-number{
        font-size:38px;
        font-weight:800;
        color:white;
    }

    .metric-label{
        color:#cbd5e1;
        margin-top:6px;
    }

    .skill-pill{
        display:inline-block;
        padding:10px 18px;
        margin:6px;
        border-radius:999px;
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        color:white;
        font-weight:600;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================================================
    # HERO SECTION
    # =========================================================

    st.markdown("""
    <div class="practice-title">
        🧠 AI Mock Practice Zone
    </div>

    <div class="practice-sub">
        Personalized Technical Interview Practice • AI Generated Questions • Smart Evaluation
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # TOP METRICS
    # =========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">500+</div>
            <div class="metric-label">Question Bank</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">AI</div>
            <div class="metric-label">Generated MCQs</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">24/7</div>
            <div class="metric-label">Practice Access</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100%</div>
            <div class="metric-label">Interview Focused</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # =========================================================
    # SETTINGS PANEL
    # =========================================================

    col1, col2 = st.columns(2)

    with col1:
        difficulty = st.selectbox(
            "🎯 Select Difficulty",
            ["Beginner", "Intermediate", "Advanced"]
        )

    with col2:
        question_limit = st.slider(
            "📝 Number of Questions",
            5,
            20,
            10
        )

    st.write("")
    st.write("")

    # =========================================================
    # FILE UPLOAD
    # =========================================================

    uploaded_file = st.file_uploader(
        "📄 Upload Your Resume (PDF)",
        type=["pdf"]
    )

    # =========================================================
    # SESSION STATE
    # =========================================================

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "test_started" not in st.session_state:
        st.session_state.test_started = False

    # =========================================================
    # RESUME ANALYSIS
    # =========================================================

    if uploaded_file:

        with st.spinner("Analyzing Resume & Extracting Skills..."):

            # Extract Resume Text
            resume_text = extract_text_from_pdf(uploaded_file)

            # Extract Skills
            skills = extract_skills_db(resume_text)

        # =========================================================
        # RESUME INSIGHTS
        # =========================================================

        st.subheader("📊 Resume Insights")

        rc1, rc2, rc3 = st.columns(3)

        with rc1:
            st.metric("Detected Skills", len(skills))

        with rc2:
            st.metric("Difficulty", difficulty)

        with rc3:
            st.metric("Questions", question_limit)

        st.write("")
        st.write("")

        # =========================================================
        # DETECTED SKILLS
        # =========================================================

        st.subheader("💻 Extracted Skills")

        if skills:

            skill_html = ""

            for skill in skills:
                skill_html += f"<span class='skill-pill'>{skill.upper()}</span>"

            st.markdown(skill_html, unsafe_allow_html=True)

        else:
            st.warning("No skills detected from resume.")

        st.write("")
        st.write("")

        # =========================================================
        # SKILL ANALYTICS
        # =========================================================

        if skills:

            skill_df = pd.DataFrame({
                "Skill": skills,
                "Weight": [1]*len(skills)
            })

            fig = px.bar(
                skill_df,
                x="Skill",
                y="Weight",
                title="Detected Technology Stack"
            )

            st.plotly_chart(fig, use_container_width=True)

        # =========================================================
        # GENERATE QUESTIONS
        # =========================================================

        if skills and st.button("🚀 Generate AI Questions"):

            with st.spinner("Generating Personalized Questions..."):

                st.session_state.questions = generate_questions(skills)

                st.session_state.questions = st.session_state.questions[:question_limit]

                st.session_state.test_started = True

    # =========================================================
    # STORE USER ANSWERS
    # =========================================================

    user_answers = []

    # =========================================================
    # QUESTION SECTION
    # =========================================================

    if st.session_state.questions:

        st.write("")
        st.write("")

        st.subheader("📝 Technical Interview Questions")

        total_questions = len(st.session_state.questions)

        st.progress(0)

        for i, q in enumerate(st.session_state.questions):

            if isinstance(q, dict) and "question" in q and "options" in q:

                with st.container():

                    st.markdown(f"""
                    <div class="premium-card">
                    <h3>Question {i+1}</h3>
                    </div>
                    """, unsafe_allow_html=True)

                    st.write(q["question"])

                    selected_answer = st.radio(
                        "Choose your answer:",
                        q["options"],
                        key=f"question_{i}"
                    )

                    user_answers.append(selected_answer)

                    progress_value = int(((i+1)/total_questions)*100)

                    st.progress(progress_value)

            else:
                st.warning(f"Question {i+1} format error.")

        # =========================================================
        # SUBMIT TEST
        # =========================================================

        if st.button("✅ Submit Test"):

            valid_questions = [
                q for q in st.session_state.questions
                if isinstance(q, dict)
                and "question" in q
                and "correct_answer" in q
            ]

            if valid_questions and len(user_answers) == len(valid_questions):

                score, results = evaluate_answers(
                    valid_questions,
                    user_answers
                )

                technical_percent = int(
                    (score / len(valid_questions)) * 100
                )

                # =========================================================
                # STORE PERFORMANCE
                # =========================================================

                st.session_state.technical_score = technical_percent

                st.session_state.total_tests += 1

                if technical_percent > st.session_state.best_score:
                    st.session_state.best_score = technical_percent

                st.session_state.progress_history.append({
                    "type": "Technical",
                    "score": technical_percent
                })

                # =========================================================
                # RESULTS
                # =========================================================

                st.write("")
                st.write("")

                st.subheader("🏆 Test Results")

                r1, r2, r3 = st.columns(3)

                with r1:
                    st.metric(
                        "Score",
                        f"{technical_percent}%"
                    )

                with r2:
                    st.metric(
                        "Correct",
                        f"{score}/{len(valid_questions)}"
                    )

                with r3:
                    st.metric(
                        "Best Score",
                        f"{st.session_state.best_score}%"
                    )

                st.progress(technical_percent)

                # =========================================================
                # PERFORMANCE MESSAGE
                # =========================================================

                if technical_percent >= 80:
                    st.success("🚀 Excellent Technical Performance")

                elif technical_percent >= 60:
                    st.info("📘 Good Progress. Keep Practicing")

                else:
                    st.error("⚠️ More Practice Needed")

                # =========================================================
                # PIE CHART
                # =========================================================

                chart_df = pd.DataFrame({
                    "Category": ["Correct", "Wrong"],
                    "Value": [
                        score,
                        len(valid_questions)-score
                    ]
                })

                pie_fig = px.pie(
                    chart_df,
                    names="Category",
                    values="Value",
                    title="Performance Distribution"
                )

                st.plotly_chart(
                    pie_fig,
                    use_container_width=True
                )

                # =========================================================
                # DETAILED RESULTS
                # =========================================================

                st.subheader("📄 Answer Evaluation")

                for result in results:
                    st.write(result)

                # =========================================================
                # AI FEEDBACK
                # =========================================================

                st.subheader("🤖 AI Feedback")

                if technical_percent >= 80:
                    st.success("""
                    Strong technical knowledge detected.
                    You are highly prepared for technical interviews.
                    """)

                elif technical_percent >= 60:
                    st.info("""
                    You have decent understanding but should improve weaker topics.
                    """)

                else:
                    st.error("""
                    Focus more on technical concepts and coding fundamentals.
                    """)

            else:
                st.error("Some questions are invalid. Please regenerate.")









elif menu_bar=="Aptitude Test":

    import plotly.express as px
    import pandas as pd
    import time

    # =========================================================
    # PREMIUM CSS
    # =========================================================

    st.markdown("""
    <style>

    .stApp{
        background:
        radial-gradient(circle at top left, rgba(59,130,246,.18), transparent 25%),
        radial-gradient(circle at bottom right, rgba(168,85,247,.18), transparent 25%),
        linear-gradient(180deg,#020617,#0f172a,#111827);
    }

    .apt-title{
        font-size:58px;
        font-weight:900;
        background:linear-gradient(90deg,#ffffff,#60a5fa,#c084fc);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        margin-bottom:10px;
    }

    .apt-sub{
        color:#cbd5e1;
        font-size:19px;
        margin-bottom:35px;
        line-height:1.8;
    }

    .metric-card{
        background:rgba(17,24,39,.75);
        backdrop-filter:blur(12px);
        border-radius:24px;
        padding:25px;
        text-align:center;
        border:1px solid rgba(255,255,255,.06);
        transition:.3s;
    }

    .metric-card:hover{
        transform:translateY(-6px);
        border:1px solid #3b82f6;
        box-shadow:0 15px 35px rgba(59,130,246,.25);
    }

    .metric-number{
        font-size:42px;
        font-weight:800;
        color:white;
    }

    .metric-label{
        color:#cbd5e1;
        margin-top:8px;
    }

    .question-card{
        background:rgba(17,24,39,.78);
        backdrop-filter:blur(14px);
        border-radius:28px;
        padding:28px;
        border:1px solid rgba(255,255,255,.06);
        margin-bottom:25px;
        box-shadow:0 10px 30px rgba(0,0,0,.35);
    }

    .question-title{
        color:white;
        font-size:24px;
        font-weight:700;
        margin-bottom:15px;
    }

    .particles{
        position:fixed;
        width:100%;
        height:100%;
        top:0;
        left:0;
        z-index:-1;
        overflow:hidden;
    }

    .particles span{
        position:absolute;
        width:6px;
        height:6px;
        background:rgba(255,255,255,.15);
        border-radius:50%;
        animation:float 25s linear infinite;
        bottom:-150px;
    }

    @keyframes float{
        0%{
            transform:translateY(0) scale(0);
            opacity:0;
        }

        10%{
            opacity:1;
        }

        100%{
            transform:translateY(-1200px) scale(1);
            opacity:0;
        }
    }

    .particles span:nth-child(1){left:10%;animation-duration:18s;}
    .particles span:nth-child(2){left:20%;animation-duration:22s;}
    .particles span:nth-child(3){left:30%;animation-duration:16s;}
    .particles span:nth-child(4){left:40%;animation-duration:25s;}
    .particles span:nth-child(5){left:50%;animation-duration:20s;}
    .particles span:nth-child(6){left:60%;animation-duration:15s;}
    .particles span:nth-child(7){left:70%;animation-duration:26s;}
    .particles span:nth-child(8){left:80%;animation-duration:19s;}
    .particles span:nth-child(9){left:90%;animation-duration:24s;}

    .stButton>button{
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        color:white;
        border:none;
        padding:14px 28px;
        border-radius:14px;
        font-weight:700;
        transition:.3s;
        box-shadow:0 10px 25px rgba(37,99,235,.25);
    }

    .stButton>button:hover{
        transform:translateY(-3px);
    }

    .stProgress > div > div > div > div{
        background:linear-gradient(90deg,#3b82f6,#7c3aed);
    }

    </style>

    <div class="particles">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </div>

    """, unsafe_allow_html=True)

    # =========================================================
    # HERO SECTION
    # =========================================================

    st.markdown("""
    <div class="apt-title">
        🧠 AI Aptitude Mastery
    </div>

    <div class="apt-sub">
        Practice Quantitative Aptitude • Logical Reasoning • Placement Intelligence • AI Evaluation
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # TOP METRICS
    # =========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">1000+</div>
            <div class="metric-label">Questions</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">AI</div>
            <div class="metric-label">Generated Tests</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">24/7</div>
            <div class="metric-label">Access</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100%</div>
            <div class="metric-label">Placement Focus</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # =========================================================
    # SETTINGS
    # =========================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        category = st.selectbox(
            "📘 Select Category",
            ["Quantitative Aptitude", "Logical Reasoning"]
        )

    with col2:
        difficulty = st.selectbox(
            "🎯 Difficulty",
            ["Beginner", "Intermediate", "Advanced"]
        )

    with col3:
        question_limit = st.slider(
            "📝 Number of Questions",
            5,
            20,
            10
        )

    # =========================================================
    # SESSION STATE
    # =========================================================

    if "aptitude_questions" not in st.session_state:
        st.session_state.aptitude_questions = []

    # =========================================================
    # GENERATE QUESTIONS
    # =========================================================

    if st.button("🚀 Generate AI Aptitude Test"):

        with st.spinner("Generating Smart Aptitude Questions..."):

            st.session_state.aptitude_questions = generate_aptitude_questions(category)

            st.session_state.aptitude_questions = st.session_state.aptitude_questions[:question_limit]

    # =========================================================
    # STORE ANSWERS
    # =========================================================

    user_answers = []

    # =========================================================
    # SHOW QUESTIONS
    # =========================================================

    if st.session_state.aptitude_questions:

        st.subheader("📄 Aptitude Questions")

        total_questions = len(st.session_state.aptitude_questions)

        for i, q in enumerate(st.session_state.aptitude_questions):

            if isinstance(q, dict) and "question" in q and "options" in q:

                st.markdown(f"""
                <div class="question-card">
                    <div class="question-title">
                        Question {i+1}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.write(q["question"])

                selected_answer = st.radio(
                    "Choose your answer:",
                    q["options"],
                    key=f"aptitude_{i}"
                )

                user_answers.append(selected_answer)

                progress_value = int(((i+1)/total_questions)*100)

                st.progress(progress_value)

        # =========================================================
        # SUBMIT TEST
        # =========================================================

        if st.button("✅ Submit Aptitude Test"):

            valid_questions = [
                q for q in st.session_state.aptitude_questions
                if isinstance(q, dict)
                and "question" in q
                and "correct_answer" in q
            ]

            if valid_questions and len(user_answers) == len(valid_questions):

                score, results = evaluate_answers(
                    valid_questions,
                    user_answers
                )

                aptitude_percent = int(
                    (score / len(valid_questions)) * 100
                )

                # SAVE SCORE

                st.session_state.aptitude_score = aptitude_percent

                st.session_state.total_tests += 1

                if aptitude_percent > st.session_state.best_score:
                    st.session_state.best_score = aptitude_percent

                st.session_state.progress_history.append({
                    "type": "Aptitude",
                    "score": aptitude_percent
                })

                # =========================================================
                # RESULT METRICS
                # =========================================================

                st.subheader("🏆 Performance Analytics")

                r1, r2, r3 = st.columns(3)

                with r1:
                    st.metric(
                        "Final Score",
                        f"{aptitude_percent}%"
                    )

                with r2:
                    st.metric(
                        "Correct Answers",
                        f"{score}/{len(valid_questions)}"
                    )

                with r3:
                    st.metric(
                        "Best Score",
                        f"{st.session_state.best_score}%"
                    )

                st.progress(aptitude_percent)

                # =========================================================
                # PERFORMANCE MESSAGE
                # =========================================================

                if aptitude_percent >= 80:
                    st.success("🚀 Excellent Aptitude Skills")

                elif aptitude_percent >= 60:
                    st.info("📘 Good Progress. Keep Improving")

                else:
                    st.error("⚠️ More Aptitude Practice Needed")

                # =========================================================
                # PREMIUM PIE CHART
                # =========================================================

                chart_df = pd.DataFrame({
                    "Category": ["Correct", "Wrong"],
                    "Value": [
                        score,
                        len(valid_questions)-score
                    ]
                })

                pie_fig = px.pie(
                    chart_df,
                    names="Category",
                    values="Value",
                    hole=0.45,
                    title="Performance Distribution"
                )

                pie_fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="white"),
                    height=500
                )

                st.plotly_chart(
                    pie_fig,
                    use_container_width=True
                )

                # =========================================================
                # RESULTS
                # =========================================================

                st.subheader("📋 Detailed Evaluation")

                for result in results:
                    st.write(result)

                # =========================================================
                # AI FEEDBACK
                # =========================================================

                st.subheader("🤖 AI Performance Insights")

                if aptitude_percent >= 80:

                    st.success("""
                    Strong quantitative and logical reasoning skills detected.
                    You are highly placement ready.
                    """)

                elif aptitude_percent >= 60:

                    st.info("""
                    Good aptitude foundation.
                    Continue practicing speed and accuracy.
                    """)

                else:

                    st.error("""
                    Focus more on quantitative aptitude and reasoning practice.
                    """)

            else:
                st.error("Some questions are invalid. Please regenerate.")













elif menu_bar=="Dashboard":

    import plotly.express as px
    import plotly.graph_objects as go
    import pandas as pd
    import numpy as np

    # =========================================================
    # PREMIUM CSS
    # =========================================================

    st.markdown("""
    <style>

    .stApp{
        background:
        radial-gradient(circle at top left, rgba(59,130,246,.18), transparent 25%),
        radial-gradient(circle at bottom right, rgba(168,85,247,.18), transparent 25%),
        linear-gradient(180deg,#020617,#0f172a,#111827);
    }

    .dashboard-title{
        font-size:60px;
        font-weight:900;
        background:linear-gradient(90deg,#ffffff,#60a5fa,#c084fc);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        margin-bottom:10px;
    }

    .dashboard-sub{
        color:#cbd5e1;
        font-size:20px;
        margin-bottom:35px;
        line-height:1.8;
    }

    .metric-card{
        background:rgba(17,24,39,.75);
        backdrop-filter:blur(14px);
        border-radius:26px;
        padding:28px;
        text-align:center;
        border:1px solid rgba(255,255,255,.06);
        transition:.35s;
        box-shadow:0 10px 30px rgba(0,0,0,.35);
    }

    .metric-card:hover{
        transform:translateY(-8px);
        border:1px solid #3b82f6;
        box-shadow:0 18px 40px rgba(59,130,246,.25);
    }

    .metric-number{
        font-size:46px;
        font-weight:800;
        color:white;
    }

    .metric-label{
        color:#cbd5e1;
        margin-top:8px;
        font-size:16px;
    }

    .glass-card{
        background:rgba(17,24,39,.72);
        backdrop-filter:blur(14px);
        border-radius:28px;
        padding:30px;
        border:1px solid rgba(255,255,255,.06);
        box-shadow:0 10px 30px rgba(0,0,0,.35);
        margin-bottom:25px;
    }

    .particles{
        position:fixed;
        width:100%;
        height:100%;
        top:0;
        left:0;
        z-index:-1;
        overflow:hidden;
    }

    .particles span{
        position:absolute;
        width:6px;
        height:6px;
        background:rgba(255,255,255,.15);
        border-radius:50%;
        animation:float 25s linear infinite;
        bottom:-150px;
    }

    @keyframes float{
        0%{
            transform:translateY(0) scale(0);
            opacity:0;
        }

        10%{
            opacity:1;
        }

        100%{
            transform:translateY(-1200px) scale(1);
            opacity:0;
        }
    }

    .particles span:nth-child(1){left:10%;animation-duration:18s;}
    .particles span:nth-child(2){left:20%;animation-duration:22s;}
    .particles span:nth-child(3){left:30%;animation-duration:16s;}
    .particles span:nth-child(4){left:40%;animation-duration:25s;}
    .particles span:nth-child(5){left:50%;animation-duration:20s;}
    .particles span:nth-child(6){left:60%;animation-duration:15s;}
    .particles span:nth-child(7){left:70%;animation-duration:26s;}
    .particles span:nth-child(8){left:80%;animation-duration:19s;}
    .particles span:nth-child(9){left:90%;animation-duration:24s;}

    </style>

    <div class="particles">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </div>

    """, unsafe_allow_html=True)

    # =========================================================
    # HERO SECTION
    # =========================================================

    st.markdown("""
    <div class="dashboard-title">
        📊 AI Performance Dashboard
    </div>

    <div class="dashboard-sub">
        Smart Analytics • AI Readiness Tracking • Performance Intelligence • Career Insights
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # FETCH SCORES
    # =========================================================

    technical_score = st.session_state.get("technical_score", 0)

    aptitude_score = st.session_state.get("aptitude_score", 0)

    total_tests = st.session_state.get("total_tests", 0)

    best_score = st.session_state.get("best_score", 0)

    overall_score = int(
        (technical_score + aptitude_score) / 2
    )

    # =========================================================
    # TOP METRICS
    # =========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{overall_score}%</div>
            <div class="metric-label">Overall Score</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{technical_score}%</div>
            <div class="metric-label">Technical</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{aptitude_score}%</div>
            <div class="metric-label">Aptitude</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{best_score}%</div>
            <div class="metric-label">Best Score</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # =========================================================
    # PERFORMANCE DATA
    # =========================================================

    performance_data = pd.DataFrame({
        "Category": ["Technical", "Aptitude"],
        "Score": [technical_score, aptitude_score]
    })

    # =========================================================
    # BAR CHART
    # =========================================================

    st.subheader("📈 Performance Comparison")

    bar_fig = px.bar(
        performance_data,
        x="Category",
        y="Score",
        text="Score",
        title="Technical vs Aptitude",
        color="Category"
    )

    bar_fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(17,24,39,.72)",
        font=dict(color="white"),
        height=500
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

    # =========================================================
    # PIE CHART
    # =========================================================

    st.subheader("🥧 Score Distribution")

    pie_fig = px.pie(
        performance_data,
        names="Category",
        values="Score",
        hole=0.5,
        title="Performance Breakdown"
    )

    pie_fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        height=500
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    # =========================================================
    # RADAR CHART
    # =========================================================

    st.subheader("🕸 Skill Radar Analysis")

    radar_fig = go.Figure()

    radar_fig.add_trace(go.Scatterpolar(
        r=[
            technical_score,
            aptitude_score,
            overall_score,
            best_score,
            max(technical_score, aptitude_score)
        ],
        theta=[
            "Technical",
            "Aptitude",
            "Overall",
            "Best",
            "Potential"
        ],
        fill='toself'
    ))

    radar_fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        height=600
    )

    st.plotly_chart(
        radar_fig,
        use_container_width=True
    )

    # =========================================================
    # PERFORMANCE HISTORY
    # =========================================================

    st.subheader("📊 Progress Timeline")

    history = st.session_state.get(
        "progress_history",
        []
    )

    if history:

        history_df = pd.DataFrame(history)

        history_df["Attempt"] = range(
            1,
            len(history_df)+1
        )

        line_fig = px.line(
            history_df,
            x="Attempt",
            y="score",
            color="type",
            markers=True,
            title="Performance Growth"
        )

        line_fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(17,24,39,.72)",
            font=dict(color="white"),
            height=500
        )

        st.plotly_chart(
            line_fig,
            use_container_width=True
        )

    else:
        st.info("No progress history available yet.")

    # =========================================================
    # AI READINESS INDEX
    # =========================================================

    st.subheader("🤖 AI Career Readiness")

    st.progress(overall_score)

    if overall_score >= 80:

        st.success("""
        🚀 Excellent! You are highly prepared for placements and technical interviews.
        """)

        career_level = "Industry Ready"

    elif overall_score >= 60:

        st.info("""
        📘 Good progress. Improve weak areas to become placement ready.
        """)

        career_level = "Almost Ready"

    else:

        st.error("""
        ⚠️ You need more structured preparation.
        """)

        career_level = "Needs Improvement"

    # =========================================================
    # SMART INSIGHTS
    # =========================================================

    st.subheader("💡 Smart Insights")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="glass-card">
        <h3 style='color:white;'>💪 Strengths</h3>
        """, unsafe_allow_html=True)

        if technical_score >= aptitude_score:
            st.success("Strong technical problem solving")

        if aptitude_score >= technical_score:
            st.success("Strong aptitude reasoning")

        if overall_score >= 80:
            st.success("Excellent interview readiness")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="glass-card">
        <h3 style='color:white;'>⚠ Areas To Improve</h3>
        """, unsafe_allow_html=True)

        if technical_score < 70:
            st.warning("Improve coding and technical MCQs")

        if aptitude_score < 70:
            st.warning("Improve aptitude speed and accuracy")

        if overall_score < 60:
            st.warning("Need more consistent practice")

        st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================
    # CAREER PREDICTION
    # =========================================================

    st.subheader("🔮 AI Career Prediction")

    if overall_score >= 85:

        st.success("""
        Recommended Roles:
        • Software Engineer
        • Data Scientist
        • AI Engineer
        • Backend Developer
        """)

    elif overall_score >= 70:

        st.info("""
        Recommended Roles:
        • Junior Developer
        • Web Developer
        • QA Engineer
        • Technical Support
        """)

    else:

        st.error("""
        Focus on strengthening:
        • Problem Solving
        • Technical Concepts
        • Aptitude Speed
        """)

    # =========================================================
    # FINAL SUMMARY
    # =========================================================

    st.subheader("📋 Dashboard Summary")

    st.info(f"""
    Overall Performance : {overall_score}%

    Technical Score : {technical_score}%

    Aptitude Score : {aptitude_score}%

    Total Tests Attempted : {total_tests}

    Career Readiness : {career_level}
    """)











elif menu_bar=="HelpBot":

    import time
    import random

    # =========================================================
    # PREMIUM CSS
    # =========================================================

    st.markdown("""
    <style>

    .stApp{
        background:
        radial-gradient(circle at top left, rgba(59,130,246,.18), transparent 25%),
        radial-gradient(circle at bottom right, rgba(168,85,247,.18), transparent 25%),
        linear-gradient(180deg,#020617,#0f172a,#111827);
    }

    .bot-title{
        font-size:60px;
        font-weight:900;
        background:linear-gradient(90deg,#ffffff,#60a5fa,#c084fc);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        margin-bottom:10px;
    }

    .bot-sub{
        color:#cbd5e1;
        font-size:20px;
        margin-bottom:35px;
        line-height:1.8;
    }

    .chat-user{
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        padding:18px;
        border-radius:22px 22px 5px 22px;
        color:white;
        margin-bottom:15px;
        margin-left:120px;
        box-shadow:0 10px 25px rgba(37,99,235,.25);
        animation:fadeIn .4s ease;
    }

    .chat-bot{
        background:rgba(17,24,39,.78);
        backdrop-filter:blur(14px);
        border:1px solid rgba(255,255,255,.06);
        padding:18px;
        border-radius:22px 22px 22px 5px;
        color:white;
        margin-bottom:18px;
        margin-right:120px;
        box-shadow:0 10px 30px rgba(0,0,0,.35);
        animation:fadeIn .4s ease;
    }

    @keyframes fadeIn{
        from{
            opacity:0;
            transform:translateY(10px);
        }

        to{
            opacity:1;
            transform:translateY(0);
        }
    }

    .metric-card{
        background:rgba(17,24,39,.75);
        backdrop-filter:blur(14px);
        border-radius:24px;
        padding:24px;
        text-align:center;
        border:1px solid rgba(255,255,255,.06);
        transition:.3s;
        margin-bottom:20px;
    }

    .metric-card:hover{
        transform:translateY(-6px);
        border:1px solid #3b82f6;
        box-shadow:0 15px 35px rgba(59,130,246,.25);
    }

    .metric-number{
        font-size:42px;
        font-weight:800;
        color:white;
    }

    .metric-label{
        color:#cbd5e1;
        margin-top:8px;
    }

    .suggestion-card{
        background:rgba(17,24,39,.65);
        border-radius:18px;
        padding:18px;
        border:1px solid rgba(255,255,255,.05);
        color:white;
        margin-bottom:15px;
        transition:.3s;
    }

    .suggestion-card:hover{
        transform:translateY(-4px);
        border:1px solid #7c3aed;
    }

    .particles{
        position:fixed;
        width:100%;
        height:100%;
        top:0;
        left:0;
        z-index:-1;
        overflow:hidden;
    }

    .particles span{
        position:absolute;
        width:6px;
        height:6px;
        background:rgba(255,255,255,.15);
        border-radius:50%;
        animation:float 25s linear infinite;
        bottom:-150px;
    }

    @keyframes float{
        0%{
            transform:translateY(0) scale(0);
            opacity:0;
        }

        10%{
            opacity:1;
        }

        100%{
            transform:translateY(-1200px) scale(1);
            opacity:0;
        }
    }

    .particles span:nth-child(1){left:10%;animation-duration:18s;}
    .particles span:nth-child(2){left:20%;animation-duration:22s;}
    .particles span:nth-child(3){left:30%;animation-duration:16s;}
    .particles span:nth-child(4){left:40%;animation-duration:25s;}
    .particles span:nth-child(5){left:50%;animation-duration:20s;}
    .particles span:nth-child(6){left:60%;animation-duration:15s;}
    .particles span:nth-child(7){left:70%;animation-duration:26s;}
    .particles span:nth-child(8){left:80%;animation-duration:19s;}
    .particles span:nth-child(9){left:90%;animation-duration:24s;}

    .stTextInput>div>div>input{
        background:rgba(17,24,39,.78);
        color:white;
        border-radius:16px;
        border:1px solid rgba(255,255,255,.06);
        padding:14px;
    }

    .stButton>button{
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        color:white;
        border:none;
        padding:14px 28px;
        border-radius:14px;
        font-weight:700;
        transition:.3s;
        box-shadow:0 10px 25px rgba(37,99,235,.25);
    }

    .stButton>button:hover{
        transform:translateY(-3px);
    }

    </style>

    <div class="particles">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </div>

    """, unsafe_allow_html=True)

    # =========================================================
    # HERO SECTION
    # =========================================================

    st.markdown("""
    <div class="bot-title">
        🤖 AI Career HelpBot
    </div>

    <div class="bot-sub">
        Smart Career Guidance • Interview Help • Resume Tips • AI Powered Assistance
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # TOP METRICS
    # =========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">AI</div>
            <div class="metric-label">Powered</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">24/7</div>
            <div class="metric-label">Support</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100+</div>
            <div class="metric-label">Career Tips</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">∞</div>
            <div class="metric-label">Conversations</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # =========================================================
    # SESSION STATE
    # =========================================================

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # =========================================================
    # SUGGESTIONS
    # =========================================================

    st.subheader("💡 Suggested Questions")

    s1, s2 = st.columns(2)

    with s1:
        st.markdown("""
        <div class="suggestion-card">
        🚀 How can I improve my resume?
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="suggestion-card">
        💻 Best skills for software engineers?
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown("""
        <div class="suggestion-card">
        🎯 How to crack technical interviews?
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="suggestion-card">
        📘 Tips for aptitude preparation?
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # =========================================================
    # USER INPUT
    # =========================================================

    user_query = st.text_input(
        "💬 Ask Your Career Question"
    )

    # =========================================================
    # SEND BUTTON
    # =========================================================

    if st.button("🚀 Ask AI HelpBot"):

        if user_query:

            # USER CHAT

            st.session_state.chat_history.append(
                ("user", user_query)
            )

            # =========================================================
            # EXISTING LLM RESPONSE LOGIC
            # =========================================================

            with st.spinner("AI is thinking..."):

                try:

                    # KEEP YOUR EXISTING MODEL FUNCTION HERE
                    response = chatbot_response(user_query)

                except:

                    response = """
                    I can help with:
                    • Resume Improvement
                    • Technical Interviews
                    • Aptitude Preparation
                    • Career Guidance
                    • Placement Preparation
                    """

            # BOT CHAT

            st.session_state.chat_history.append(
                ("bot", response)
            )

    # =========================================================
    # CHAT DISPLAY
    # =========================================================

    st.subheader("🧠 Conversation")

    for sender, message in st.session_state.chat_history:

        if sender == "user":

            st.markdown(f"""
            <div class="chat-user">
                <b>👤 You</b><br><br>
                {message}
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="chat-bot">
                <b>🤖 AI HelpBot</b><br><br>
                {message}
            </div>
            """, unsafe_allow_html=True)

    # =========================================================
    # AI INSIGHTS
    # =========================================================

    st.write("")
    st.write("")

    st.subheader("📊 AI Assistant Insights")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
        🔥 Trending Topics:
        • Resume Optimization
        • DSA Preparation
        • AI/ML Careers
        • Placement Readiness
        """)

    with col2:

        st.success("""
        🚀 Recommended Focus:
        • Build Strong Projects
        • Improve Aptitude Speed
        • Practice Mock Interviews
        • Optimize LinkedIn Profile
        """)













    from langchain_community.chat_models import ChatOllama
    from langchain_community.llms import Ollama
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough, RunnableLambda
    import streamlit as st


    llm = Ollama(model="llama3.2")
    chat = ChatOllama(model="llama3.2")


    file_text = ""


    def fake_retriever(query: str) -> str:
        global file_text
        if file_text:
            return file_text[:1000]   # limit context
        return "No file uploaded. Answer from general knowledge."

    rag_prompt = ChatPromptTemplate.from_template(
        """Use only the following context to answer the question.
        Context: {context}
        Question: {question}
        Answer:"""
    )


    rag_chain = (
        RunnablePassthrough.assign(
            context=RunnableLambda(lambda x: fake_retriever(x["question"]))
        )
        | rag_prompt
        | chat
        | StrOutputParser()
    )


    def ask_rag(question):
        return rag_chain.invoke({"question": question})


    st.set_page_config(layout="wide")



    if "messages" not in st.session_state:
        st.session_state.messages = []


    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


    
    user_input = st.chat_input("Ask Anything....")

    if user_input:
        
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask_rag(user_input)
                st.markdown(response)

        
        st.session_state.messages.append({"role": "assistant", "content": response})






elif menu_bar == "AboutUs":

    st.markdown("""
    <style>

    .stApp{
        background:
        radial-gradient(circle at top left, rgba(59,130,246,.18), transparent 25%),
        radial-gradient(circle at bottom right, rgba(168,85,247,.18), transparent 25%),
        linear-gradient(180deg,#020617,#0f172a,#111827);
    }

    .hero-box{
        padding:70px;
        border-radius:35px;
        background:
        radial-gradient(circle at top right, rgba(59,130,246,.28), transparent 30%),
        radial-gradient(circle at bottom left, rgba(168,85,247,.25), transparent 30%),
        linear-gradient(135deg,#0f172a,#1e293b,#111827);

        border:1px solid rgba(255,255,255,.08);
        box-shadow:0 25px 60px rgba(0,0,0,.4);
        margin-bottom:35px;
    }

    .hero-title{
        font-size:68px;
        font-weight:900;
        line-height:1.1;
        color:white;
        margin-bottom:20px;
    }

    .hero-sub{
        font-size:20px;
        color:#cbd5e1;
        line-height:1.9;
    }

    .glass-card{
        background:rgba(17,24,39,.72);
        backdrop-filter:blur(14px);
        border-radius:28px;
        padding:30px;
        border:1px solid rgba(255,255,255,.06);
        box-shadow:0 10px 30px rgba(0,0,0,.35);
        transition:.35s;
        height:100%;
    }

    .glass-card:hover{
        transform:translateY(-8px);
        border:1px solid #3b82f6;
        box-shadow:0 20px 45px rgba(59,130,246,.25);
    }

    .card-icon{
        font-size:50px;
        margin-bottom:15px;
    }

    .card-title{
        color:white;
        font-size:28px;
        font-weight:700;
        margin-bottom:10px;
    }

    .card-desc{
        color:#cbd5e1;
        line-height:1.8;
    }

    .section-title{
        color:white;
        font-size:42px;
        font-weight:800;
        margin-top:20px;
        margin-bottom:25px;
    }

    .metric-card{
        background:linear-gradient(145deg,#111827,#1e293b);
        padding:28px;
        border-radius:24px;
        text-align:center;
        border:1px solid rgba(255,255,255,.06);
        box-shadow:0 10px 25px rgba(0,0,0,.25);
    }

    .metric-number{
        font-size:42px;
        font-weight:800;
        color:white;
    }

    .metric-label{
        color:#cbd5e1;
        margin-top:8px;
    }

    .timeline-card{
        background:rgba(17,24,39,.72);
        border-left:5px solid #3b82f6;
        padding:24px;
        border-radius:20px;
        color:white;
        margin-bottom:20px;
        box-shadow:0 10px 25px rgba(0,0,0,.25);
    }

    .footer-box{
        margin-top:50px;
        padding:55px;
        border-radius:30px;
        text-align:center;
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        color:white;
        box-shadow:0 20px 45px rgba(59,130,246,.3);
    }

    .stTextInput>div>div>input{
        background:rgba(17,24,39,.78);
        color:white;
        border-radius:14px;
        border:1px solid rgba(255,255,255,.08);
    }

    .stTextArea textarea{
        background:rgba(17,24,39,.78);
        color:white;
        border-radius:14px;
        border:1px solid rgba(255,255,255,.08);
    }

    .stButton>button{
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        color:white;
        border:none;
        padding:14px 28px;
        border-radius:14px;
        font-weight:700;
        transition:.3s;
        box-shadow:0 10px 25px rgba(37,99,235,.25);
    }

    .stButton>button:hover{
        transform:translateY(-3px);
    }

    </style>
    """, unsafe_allow_html=True)

    # HERO SECTION

    st.markdown("""
<style>

.hero-title{
    font-size:65px;
    font-weight:900;
    color:white;
    margin-bottom:20px;
}

.hero-sub{
    font-size:20px;
    color:#cbd5e1;
    line-height:1.8;
}

</style>

<div class="hero-title">
    🚀 About Resume Vision AI
</div>

<div class="hero-sub">
    Resume Vision AI is a premium AI-powered interview preparation platform
    designed to help students crack placements, improve resumes,
    practice technical interviews, solve aptitude questions,
    and become industry ready with smart analytics.
</div>

""", unsafe_allow_html=True)

    # METRICS

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">AI</div>
            <div class="metric-label">Powered</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">24/7</div>
            <div class="metric-label">Access</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">1000+</div>
            <div class="metric-label">Questions</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100%</div>
            <div class="metric-label">Placement Focus</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # FEATURES

    st.markdown("""
    <div class="section-title">
        ✨ Premium Features
    </div>
    """, unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">📄</div>
            <div class="card-title">Resume Intelligence</div>
            <div class="card-desc">
                AI-powered ATS analysis with resume optimization,
                skill detection, and smart improvement suggestions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">🧠</div>
            <div class="card-title">Practice Zone</div>
            <div class="card-desc">
                Personalized technical interview questions
                generated using AI based on your skills.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">📊</div>
            <div class="card-title">Analytics Dashboard</div>
            <div class="card-desc">
                Smart analytics, performance tracking,
                and career readiness monitoring.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # JOURNEY

    st.markdown("""
    <div class="section-title">
        🛤 Your AI Journey
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-card">
        <h3>1️⃣ Upload Resume</h3>
        <p>Upload your resume for AI-powered analysis.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-card">
        <h3>2️⃣ Extract Skills</h3>
        <p>AI automatically detects technologies and strengths.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-card">
        <h3>3️⃣ Practice Interviews</h3>
        <p>Attempt personalized technical and aptitude questions.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-card">
        <h3>4️⃣ Track Performance</h3>
        <p>Analyze your growth with smart visual dashboards.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # TECHNOLOGY STACK

    st.markdown("""
    <div class="section-title">
        ⚡ Technology Stack
    </div>
    """, unsafe_allow_html=True)

    t1, t2, t3, t4 = st.columns(4)

    with t1:
        st.success("🐍 Python")

    with t2:
        st.success("🎈 Streamlit")

    with t3:
        st.success("🤖 Ollama")

    with t4:
        st.success("🧠 Llama 3")

    st.write("")
    st.write("")

    # FEEDBACK SECTION

    st.markdown("""
    <div class="section-title">
        💬 Feedback
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Your Name")

    feedback = st.text_area("Write Your Feedback")

    if st.button("🚀 Submit Feedback"):

        if name and feedback:
            st.success("✅ Thank you for your feedback!")

        else:
            st.warning("Please fill all fields.")

    # FOOTER

    # st.markdown("""
    # <div class="footer-box">

    #     <h1>
    #         🚀 Build Your Future With AI
    #     </h1>

    #     <p style="font-size:20px; margin-top:15px;">
    #         Resume Vision AI helps students become placement ready
    #         with smart AI-powered preparation tools.
    #     </p>

    # </div>
    # """, unsafe_allow_html=True)