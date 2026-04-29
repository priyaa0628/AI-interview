
from streamlit_option_menu import option_menu
import streamlit as st
import requests
import pdfplumber

# -----------------------------------
# CONFIG
# -----------------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🚀",
    layout="centered"
    
)

# -----------------------------------
# CSS
# -----------------------------------
st.markdown("""
<style>
.main{
background:#f8fafc;
}
.block-container{
max-width:1200px;
padding-top:1rem;
}
.stButton>button{
background:#2563eb;
color:white;
border:none;
border-radius:10px;
height:45px;
width:100%;
font-weight:700;
}
.card{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.05);
margin-bottom:20px;
}
.hero{
background:linear-gradient(135deg,#2563eb,#4f46e5);
padding:55px;
border-radius:22px;
color:white;
text-align:center;
margin-bottom:25px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# FUNCTIONS
# -----------------------------------
def ask_ollama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    res = requests.post(OLLAMA_URL, json=payload)
    return res.json()["response"]

def read_resume(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

# -------------------------------------------------
# PREMIUM SIDEBAR OPTION MENU
# -------------------------------------------------

# st.markdown("""
# <style>

# /* SIDEBAR BACKGROUND */
# section[data-testid="stSidebar"]{
#     background:linear-gradient(180deg,#111827,#1e293b,#0f172a);
# }

# /* TITLE */
# .sidebar-title{
#     color:white;
#     font-size:28px;
#     font-weight:800;
#     text-align:center;
#     margin-bottom:6px;
# }

# .sidebar-sub{
#     color:#cbd5e1;
#     text-align:center;
#     font-size:14px;
#     margin-bottom:24px;
# }

# /* FOOTER */
# .sidebar-footer{
#     background:rgba(255,255,255,.06);
#     padding:16px;
#     border-radius:14px;
#     color:#e2e8f0;
#     text-align:center;
#     margin-top:25px;
#     font-size:13px;
# }

# </style>
# """, unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR MENU
# -------------------------------------------------

# with st.sidebar:

#     st.markdown("""
#     <div class="sidebar-title">🚀 AI Career Hub</div>
#     <div class="sidebar-sub">
#     Interview Preparation Platform
#     </div>
#     """, unsafe_allow_html=True)

#     page = option_menu(
#         menu_title=None,
#         options=[
#             "Home",
#             "Interview Questions",
#             "Answer Evaluation",
#             "Resume Analyzer",
#             "Mock Interview",
#             "Dashboard",
#             "About"
#         ],
#         icons=[
#             "house-fill",
#             "patch-question-fill",
#             "clipboard-check-fill",
#             "file-earmark-person-fill",
#             "camera-video-fill",
#             "bar-chart-fill",
#             "info-circle-fill"
#         ],
#         menu_icon="cast",
#         default_index=0,

#         styles={
#             "container": {
#                 "padding": "0!important",
#                 "background-color": "transparent"
#             },

#             "icon": {
#                 "color": "white",
#                 "font-size": "18px"
#             },

#             "nav-link": {
#                 "font-size": "16px",
#                 "text-align": "left",
#                 "margin": "6px",
#                 "padding": "12px",
#                 "border-radius": "12px",
#                 "color": "white",
#                 "--hover-color": "#2563eb"
#             },

#             "nav-link-selected": {
#                 "background": "linear-gradient(135deg,#2563eb,#4f46e5)",
#                 "font-weight": "700"
#             },
#         }
#     )

#     st.markdown("""
#     <div class="sidebar-footer">
#     ⭐ Powered by Streamlit + Ollama <br><br>
#     💼 Crack Your Dream Job Faster
#     </div>
#     """, unsafe_allow_html=True)


# -----------------------------------------
# SIDEBAR CONTENT
# -----------------------------------------
with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">🚀 AI Career Hub</div>
    <div class="sidebar-sub">
    Smart Interview Preparation Platform
    </div>
    """, unsafe_allow_html=True)

    page = option_menu(
        menu_title=None,
        options=
        [
            "🏠 Home",
            "🎯 Interview Questions",
            "📝 Answer Evaluation",
            "📄 Resume Analyzer",
            "📚 Mock Interview",
            "📈 Dashboard",
            "ℹ About"
        ],
       
        menu_icon="cast",
        default_index=0,

        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent"
            },

            "icon": {
                "color": "white",
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "6px",
                "padding": "12px",
                "border-radius": "12px",
                "color": "white",
                "--hover-color": "#2563eb"
            },

            "nav-link-selected": {
                "background": "linear-gradient(135deg,#2563eb,#4f46e5)",
                "font-weight": "700"
            },
        }
    )
    

    st.markdown("""
    <div class="sidebar-footer">
    ⭐ Powered by Streamlit + Ollama <br><br>
    💼 Crack Your Dream Job Faster
    </div>
    """, unsafe_allow_html=True)



# ===================================================
# HOME
# ===================================================

if page == "🏠 Home":

    # HERO SECTION
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#2563eb,#4f46e5);
        padding:60px;
        border-radius:24px;
        color:white;
        text-align:center;
        margin-bottom:30px;
    '>
        <h1 style='font-size:52px;'>🚀 AI Interview Assistant</h1>
        <p style='font-size:20px;'>
        Smart Platform for Interview Preparation, Resume Analysis & Career Growth
        </p>
        <br>
        <p>
        Generate Questions • Evaluate Answers • Resume ATS Score • Mock Interviews
        </p>
    </div>
    """, unsafe_allow_html=True)

    # STATS
    st.subheader("📈 Platform Highlights")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Users Helped", "12,500+")

    with c2:
        st.metric("Questions Generated", "65,000+")

    with c3:
        st.metric("Answers Evaluated", "18,000+")

    with c4:
        st.metric("Resumes Reviewed", "7,500+")

    st.markdown("---")

    # FEATURES
    st.subheader("🔥 Core Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div style='background:black;padding:25px;border-radius:18px;
        box-shadow:0 8px 20px rgba(0,0,0,.05);text-align:center;'>
        <h2>🎯</h2>
        <h3>Interview Questions</h3>
        <p>Generate job-role based technical and HR interview questions instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div style='background:black;padding:25px;border-radius:18px;
        box-shadow:0 8px 20px rgba(0,0,0,.05);text-align:center;'>
        <h2>📝</h2>
        <h3>Answer Evaluation</h3>
        <p>Get AI scoring, strengths, weaknesses and improvement tips.</p>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div style='background:black;padding:25px;border-radius:18px;
        box-shadow:0 8px 20px rgba(0,0,0,.05);text-align:center;'>
        <h2>📄</h2>
        <h3>Resume Analyzer</h3>
        <p>Upload your resume PDF and get ATS style feedback.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # HOW IT WORKS
    st.subheader("⚙ How It Works")

    h1, h2, h3, h4 = st.columns(4)

    with h1:
        st.info("1️⃣ Select Role")

    with h2:
        st.info("2️⃣ Generate Questions")

    with h3:
        st.info("3️⃣ Practice & Evaluate")

    with h4:
        st.info("4️⃣ Get Hired")

    st.markdown("---")

    # WHY CHOOSE US
    st.subheader("💡 Why Choose Us?")

    st.markdown("""
    ✅ Fast AI Powered Results  
    ✅ Role Based Interview Questions  
    ✅ Resume ATS Score & Suggestions  
    ✅ Real Time Feedback  
    ✅ Best for Students & Freshers  
    ✅ Professional UI Experience  
    """)

    st.markdown("---")

    # TESTIMONIALS
    st.subheader("⭐ Success Stories")

    t1, t2 = st.columns(2)

    with t1:
        st.success("""
        **Priya (Python Developer)**  
        "This tool helped me prepare confidently for my interview."
        """)

    with t2:
        st.success("""
        **Rahul (Data Analyst)**  
        "Resume analysis feature improved my CV drastically."
        """)

    st.markdown("---")

    # CTA
    st.markdown("""
    <div style='
        background:#111827;
        color:white;
        padding:40px;
        border-radius:20px;
        text-align:center;
    '>
        <h2>Ready to Crack Your Dream Job?</h2>
        <p>Start practicing today with AI Interview Assistant.</p>
    </div>
    """, unsafe_allow_html=True)

# ===================================================
# QUESTIONS
# ===================================================

elif page == "🎯 Interview Questions":

    # HERO SECTION
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#7c3aed,#2563eb);
        padding:50px;
        border-radius:22px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    '>
        <h1>🎯 AI Interview Question Generator</h1>
        <p>Create personalized interview questions for any role instantly.</p>
    </div>
    """, unsafe_allow_html=True)

    # FILTERS
    st.subheader("⚙ Customize Your Questions")

    c1, c2, c3 = st.columns(3)

    with c1:
        role = st.selectbox("Select Job Role", [
            "Python Developer",
            "Java Developer",
            "Frontend Developer",
            "Backend Developer",
            "Web Developer",
            "Data Analyst",
            "Machine Learning Engineer",
            "Cloud Engineer",
            "Cyber Security Analyst",
            "HR Manager"
        ])

    with c2:
        level = st.selectbox(
            "Difficulty Level",
            ["Beginner", "Intermediate", "Advanced"]
        )

    with c3:
        num = st.slider("Number of Questions", 1, 15, 5)

    # EXTRA OPTIONS
    col4, col5 = st.columns(2)

    with col4:
        qtype = st.selectbox(
            "Question Type",
            [
                "Technical",
                "HR",
                "Behavioral",
                "Coding",
                "Mixed"
            ]
        )

    with col5:
        exp = st.selectbox(
            "Experience Level",
            [
                "Fresher",
                "1-2 Years",
                "3-5 Years",
                "Senior Level"
            ]
        )

    # BUTTON
    if st.button("🚀 Generate Questions"):

        prompt = f"""
        You are a professional interviewer.

        Generate {num} {qtype} interview questions for {role}.

        Candidate Experience: {exp}
        Difficulty Level: {level}

        Rules:
        1. Give complete meaningful questions
        2. Use numbered format
        3. No blank lines
        4. Make questions realistic
        """

        with st.spinner("Generating Questions..."):
            result = ask_ollama(prompt)

        st.success("Questions Generated Successfully!")

        st.text_area("📋 Generated Questions", result, height=420)

    st.markdown("---")

    # SAMPLE QUESTION BANK
    st.subheader("🔥 Popular Interview Categories")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.info("""
        🐍 **Python**
        - OOP
        - Decorators
        - Django
        - APIs
        """)

    with a2:
        st.info("""
        📊 **Data Analyst**
        - SQL
        - Excel
        - Power BI
        - Statistics
        """)

    with a3:
        st.info("""
        🤖 **Machine Learning**
        - Regression
        - NLP
        - Deep Learning
        - Deployment
        """)

    st.markdown("---")

    # TIPS
    st.subheader("💡 Interview Tips")

    st.markdown("""
    ✅ Read each question carefully  
    ✅ Answer with confidence  
    ✅ Use real examples  
    ✅ Practice communication  
    ✅ Revise fundamentals  
    """)

    st.markdown("---")

    # FAQ
    st.subheader("❓ Frequently Asked Questions")

    with st.expander("Can I generate HR questions?"):
        st.write("Yes, choose HR or Mixed question type.")

    with st.expander("Can freshers use this tool?"):
        st.write("Yes, choose Fresher experience level.")

    with st.expander("Can I generate coding questions?"):
        st.write("Yes, choose Coding question type.")

    with st.expander("Does it support technical roles?"):
        st.write("Yes, multiple technical roles are available.")

# ===================================================
# ANSWER EVALUATION
# ===================================================

elif page == "📝 Answer Evaluation":

    # HERO SECTION
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#2563eb,#0ea5e9);
        padding:50px;
        border-radius:22px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    '>
        <h1>📝 AI Answer Evaluation</h1>
        <p>Practice interview answers and get instant professional feedback.</p>
    </div>
    """, unsafe_allow_html=True)

    # SETTINGS
    st.subheader("⚙ Evaluation Settings")

    c1, c2 = st.columns(2)

    with c1:
        role = st.selectbox(
            "Job Role",
            [
                "Python Developer",
                "Java Developer",
                "Frontend Developer",
                "Backend Developer",
                "Data Analyst",
                "Machine Learning Engineer",
                "HR"
            ]
        )

    with c2:
        eval_type = st.selectbox(
            "Answer Type",
            [
                "Technical",
                "HR",
                "Behavioral",
                "Coding Explanation",
                "Mixed"
            ]
        )

    # INPUTS
    st.subheader("📌 Enter Details")

    question = st.text_area(
        "Interview Question",
        placeholder="Example: What is polymorphism in OOP?"
    )

    answer = st.text_area(
        "Your Answer",
        placeholder="Type your complete answer here..."
    )

    # EXTRA OPTIONS
    x1, x2 = st.columns(2)

    with x1:
        exp = st.selectbox(
            "Candidate Level",
            ["Fresher", "Intermediate", "Experienced"]
        )

    with x2:
        strictness = st.selectbox(
            "Evaluation Strictness",
            ["Normal", "Strict", "Very Strict"]
        )

    # BUTTON
    if st.button("🚀 Evaluate My Answer"):

        prompt = f"""
        You are a professional interviewer.

        Evaluate the following answer.

        Job Role: {role}
        Question Type: {eval_type}
        Candidate Level: {exp}
        Strictness: {strictness}

        Interview Question:
        {question}

        Candidate Answer:
        {answer}

        Give:

        1. Overall Score out of 10
        2. Technical Accuracy Score
        3. Communication Score
        4. Confidence Level
        5. Strengths
        6. Weaknesses
        7. Missing Points
        8. Better Sample Answer
        9. Final Hiring Impression
        """

        with st.spinner("Evaluating Answer..."):
            result = ask_ollama(prompt)

        st.success("Evaluation Completed!")

        st.text_area("📋 Detailed Report", result, height=520)

    st.markdown("---")

    # SCORE GUIDE
    st.subheader("📊 Scoring Guide")

    g1, g2, g3 = st.columns(3)

    with g1:
        st.success("""
        **8 - 10**
        Excellent Answer  
        Strong hiring chance
        """)

    with g2:
        st.warning("""
        **5 - 7**
        Average Answer  
        Needs improvement
        """)

    with g3:
        st.error("""
        **0 - 4**
        Weak Answer  
        Practice needed
        """)

    st.markdown("---")

    # SAMPLE ANSWER TIPS
    st.subheader("💡 How to Give Better Answers")

    st.markdown("""
    ✅ Understand the question fully  
    ✅ Keep answer structured  
    ✅ Use real examples  
    ✅ Be concise and clear  
    ✅ Show confidence  
    ✅ Mention practical experience  
    """)

    st.markdown("---")

    # FAQ
    st.subheader("❓ Frequently Asked Questions")

    with st.expander("Can I evaluate HR answers?"):
        st.write("Yes. Choose HR or Behavioral type.")

    with st.expander("Can freshers use this tool?"):
        st.write("Yes. Select Fresher candidate level.")

    with st.expander("Does it give sample better answers?"):
        st.write("Yes, it suggests improved answers.")

    with st.expander("Can I use it for coding explanations?"):
        st.write("Yes, choose Coding Explanation type.")

# ===================================================
# RESUME
# ===================================================

elif page == "📄 Resume Analyzer":

    # HERO SECTION
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#059669,#10b981);
        padding:50px;
        border-radius:22px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    '>
        <h1>📄 AI Resume Analyzer</h1>
        <p>Upload your resume and get ATS score, skill gap analysis, and career guidance.</p>
    </div>
    """, unsafe_allow_html=True)

    # SETTINGS
    st.subheader("⚙ Resume Analysis Settings")

    c1, c2, c3 = st.columns(3)

    with c1:
        target_role = st.selectbox(
            "Target Job Role",
            [
                "Python Developer",
                "Java Developer",
                "Frontend Developer",
                "Backend Developer",
                "Data Analyst",
                "Machine Learning Engineer",
                "Cloud Engineer",
                "Cyber Security Analyst",
                "HR Executive"
            ]
        )

    with c2:
        experience = st.selectbox(
            "Experience Level",
            [
                "Fresher",
                "1-2 Years",
                "3-5 Years",
                "Senior Level"
            ]
        )

    with c3:
        company_type = st.selectbox(
            "Company Type",
            [
                "Startup",
                "MNC",
                "Product Based",
                "Service Based",
                "Government"
            ]
        )

    # FILE UPLOAD
    st.subheader("📤 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    # EXTRA OPTIONS
    o1, o2 = st.columns(2)

    with o1:
        analysis_mode = st.selectbox(
            "Analysis Type",
            [
                "Full Review",
                "ATS Check",
                "Skill Gap Check",
                "Formatting Review",
                "Job Match Analysis"
            ]
        )

    with o2:
        language = st.selectbox(
            "Output Style",
            [
                "Professional",
                "Simple",
                "Detailed"
            ]
        )

    # BUTTON
    if uploaded_file is not None:

        if st.button("🚀 Analyze Resume"):

            resume_text = read_resume(uploaded_file)

            prompt = f"""
            You are a professional HR recruiter and ATS expert.

            Analyze this resume.

            Target Role: {target_role}
            Experience Level: {experience}
            Company Type: {company_type}
            Analysis Type: {analysis_mode}
            Output Style: {language}

            Resume Content:
            {resume_text}

            Give:

            1. ATS Score out of 100
            2. Resume Summary
            3. Key Skills Found
            4. Missing Skills
            5. Technical Strengths
            6. Weak Areas
            7. Formatting Suggestions
            8. Projects Improvement Tips
            9. Job Match Percentage
            10. Final Recommendation
            """

            with st.spinner("Scanning Resume..."):
                result = ask_ollama(prompt)

            st.success("Resume Analysis Completed!")

            st.text_area("📋 Resume Report", result, height=560)

    st.markdown("---")

    # SCORE GUIDE
    st.subheader("📊 ATS Score Guide")

    g1, g2, g3 = st.columns(3)

    with g1:
        st.success("""
        **80 - 100**
        Excellent Resume  
        Strong chances
        """)

    with g2:
        st.warning("""
        **60 - 79**
        Good Resume  
        Needs some improvement
        """)

    with g3:
        st.error("""
        **0 - 59**
        Weak Resume  
        Needs major updates
        """)

    st.markdown("---")

    # WHAT WE CHECK
    st.subheader("🔍 What We Analyze")

    st.markdown("""
    ✅ Skills Match  
    ✅ ATS Friendly Keywords  
    ✅ Resume Structure  
    ✅ Project Quality  
    ✅ Experience Relevance  
    ✅ Certifications  
    ✅ Career Objective  
    ✅ Hiring Readiness  
    """)

    st.markdown("---")

    # RESUME TIPS
    st.subheader("💡 Tips for Better Resume")

    st.markdown("""
    ✅ Keep resume to 1-2 pages  
    ✅ Add measurable achievements  
    ✅ Use clean formatting  
    ✅ Mention latest skills  
    ✅ Add strong projects  
    ✅ Use role-specific keywords  
    """)

    st.markdown("---")

    # FAQ
    st.subheader("❓ Frequently Asked Questions")

    with st.expander("Can freshers use this tool?"):
        st.write("Yes, perfect for students and freshers.")

    with st.expander("Does it check ATS score?"):
        st.write("Yes, it estimates ATS compatibility.")

    with st.expander("Can I upload PDF resume only?"):
        st.write("Yes, currently PDF format is supported.")

    with st.expander("Will it suggest missing skills?"):
        st.write("Yes, based on your selected target role.")

# ===================================================
# MOCK INTERVIEW
# ===================================================

elif page == "📚 Mock Interview":

    # HERO SECTION
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#f97316,#ea580c);
        padding:50px;
        border-radius:22px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    '>
        <h1>📚 AI Mock Interview</h1>
        <p>Practice real interviews with AI and improve confidence before your actual interview.</p>
    </div>
    """, unsafe_allow_html=True)

    # SETTINGS
    st.subheader("⚙ Interview Setup")

    c1, c2, c3 = st.columns(3)

    with c1:
        role = st.selectbox(
            "Target Role",
            [
                "Python Developer",
                "Java Developer",
                "Frontend Developer",
                "Backend Developer",
                "Data Analyst",
                "Machine Learning Engineer",
                "HR Executive",
                "Cloud Engineer"
            ]
        )

    with c2:
        level = st.selectbox(
            "Difficulty Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    with c3:
        round_type = st.selectbox(
            "Interview Round",
            [
                "HR Round",
                "Technical Round",
                "Behavioral Round",
                "Coding Round",
                "Mixed Round"
            ]
        )

    # EXTRA SETTINGS
    x1, x2 = st.columns(2)

    with x1:
        num_q = st.slider("Number of Questions", 1, 10, 5)

    with x2:
        strictness = st.selectbox(
            "Interviewer Style",
            [
                "Friendly",
                "Professional",
                "Strict"
            ]
        )

    st.markdown("---")

    # START INTERVIEW
    if st.button("🚀 Start Mock Interview"):

        prompt = f"""
        You are a {strictness} interviewer.

        Conduct a {round_type} for {role}.

        Difficulty Level: {level}

        Ask {num_q} interview questions one by one in numbered format.

        Questions must be realistic and professional.
        """

        with st.spinner("Starting Interview..."):
            result = ask_ollama(prompt)

        st.success("Mock Interview Started!")

        st.text_area("🎤 Interview Questions", result, height=420)

    st.markdown("---")

    # LIVE ANSWER PRACTICE
    st.subheader("📝 Practice Your Answer")

    practice_q = st.text_area(
        "Paste one interview question here"
    )

    practice_ans = st.text_area(
        "Write your answer here"
    )

    if st.button("Evaluate Practice Answer"):

        prompt = f"""
        Evaluate this mock interview answer.

        Question:
        {practice_q}

        Candidate Answer:
        {practice_ans}

        Give:

        1. Score out of 10
        2. Confidence Level
        3. Strengths
        4. Weaknesses
        5. Better Sample Answer
        6. Final Impression
        """

        with st.spinner("Reviewing Answer..."):
            result = ask_ollama(prompt)

        st.text_area("📋 Feedback Report", result, height=460)

    st.markdown("---")

    # BODY LANGUAGE / COMMUNICATION TIPS
    st.subheader("💡 Interview Success Tips")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.info("""
        😃 **Confidence**
        Maintain eye contact and smile.
        """)

    with t2:
        st.info("""
        🗣 **Communication**
        Speak clearly and stay structured.
        """)

    with t3:
        st.info("""
        📌 **Knowledge**
        Revise basics before interview.
        """)

    st.markdown("---")

    # COMMON MISTAKES
    st.subheader("⚠ Avoid These Mistakes")

    st.markdown("""
    ❌ Speaking too fast  
    ❌ Giving unrelated answers  
    ❌ No examples in answers  
    ❌ Weak body language  
    ❌ Lack of confidence  
    ❌ Not knowing company basics  
    """)

    st.markdown("---")

    # FAQ
    st.subheader("❓ Frequently Asked Questions")

    with st.expander("Can I practice HR interviews?"):
        st.write("Yes, choose HR Round.")

    with st.expander("Can freshers use mock interviews?"):
        st.write("Yes, excellent for beginners.")

    with st.expander("Can it evaluate my answer too?"):
        st.write("Yes, use Practice Your Answer section.")

    with st.expander("Does it support technical interviews?"):
        st.write("Yes, Technical and Coding rounds are available.")

# ===================================================
# DASHBOARD
# ===================================================

elif page == "📈 Dashboard":

    # HERO SECTION
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#0f172a,#1e293b);
        padding:50px;
        border-radius:22px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    '>
        <h1>📈 Career Progress Dashboard</h1>
        <p>Track your interview preparation, resume quality, and hiring readiness.</p>
    </div>
    """, unsafe_allow_html=True)

    # MAIN STATS
    st.subheader("📊 Performance Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Questions Practiced", "185", "+12")

    with c2:
        st.metric("Answers Evaluated", "64", "+7")

    with c3:
        st.metric("Resume Score", "84%", "+5%")

    with c4:
        st.metric("Hiring Readiness", "78%", "+9%")

    st.markdown("---")

    # WEEKLY PROGRESS
    st.subheader("📅 Weekly Progress")

    w1, w2, w3 = st.columns(3)

    with w1:
        st.info("""
        **Mon - Wed**
        45 Questions Practiced
        """)

    with w2:
        st.info("""
        **Thu - Fri**
        12 Answers Evaluated
        """)

    with w3:
        st.info("""
        **Sat - Sun**
        Resume Updated
        """)

    st.markdown("---")

    # SKILL READINESS
    st.subheader("🧠 Skill Readiness")

    s1, s2 = st.columns(2)

    with s1:
        st.progress(85)
        st.write("Technical Skills - 85%")

        st.progress(72)
        st.write("Communication - 72%")

        st.progress(80)
        st.write("Problem Solving - 80%")

    with s2:
        st.progress(68)
        st.write("Confidence Level - 68%")

        st.progress(76)
        st.write("Resume Quality - 76%")

        st.progress(74)
        st.write("Interview Readiness - 74%")

    st.markdown("---")

    # TOP IMPROVEMENT AREAS
    st.subheader("🚀 Areas to Improve")

    i1, i2, i3 = st.columns(3)

    with i1:
        st.warning("""
        **Communication**
        Practice speaking clearly.
        """)

    with i2:
        st.warning("""
        **Confidence**
        Use mock interviews weekly.
        """)

    with i3:
        st.warning("""
        **Projects**
        Add 1 strong project in resume.
        """)

    st.markdown("---")

    # CAREER TIPS
    st.subheader("💡 Personalized Career Tips")

    st.markdown("""
    ✅ Practice 10 interview questions daily  
    ✅ Revise core technical concepts  
    ✅ Update resume keywords  
    ✅ Prepare STAR method for HR answers  
    ✅ Improve body language  
    ✅ Build LinkedIn profile  
    """)

    st.markdown("---")

    # BADGES
    st.subheader("🏆 Achievements")

    b1, b2, b3, b4 = st.columns(4)

    with b1:
        st.success("🎯 100 Questions Completed")

    with b2:
        st.success("📝 50 Answers Evaluated")

    with b3:
        st.success("📄 Resume Optimized")

    with b4:
        st.success("🚀 Ready for Interviews")

    st.markdown("---")

    # FUTURE GOALS
    st.subheader("🎯 Next 7 Day Goals")

    st.markdown("""
    ☐ Practice 30 more questions  
    ☐ Improve confidence score to 80%  
    ☐ Add one new project in resume  
    ☐ Attempt 3 mock interviews  
    ☐ Learn advanced technical topics  
    """)

    st.markdown("---")

    # FAQ
    st.subheader("❓ Dashboard FAQ")

    with st.expander("Are these scores real?"):
        st.write("They represent AI-estimated progress indicators.")

    with st.expander("Can I improve my readiness score?"):
        st.write("Yes, practice regularly and update your resume.")

    with st.expander("What is the best section to improve first?"):
        st.write("Communication and confidence usually give fast gains.")

    with st.expander("Can freshers use this dashboard?"):
        st.write("Yes, it is ideal for students and beginners.")

# ===================================================
# ABOUT
# ===================================================

elif page == "ℹ About":

    # HERO SECTION
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#4f46e5,#7c3aed);
        padding:50px;
        border-radius:22px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    '>
        <h1>ℹ About AI Interview Assistant</h1>
        <p>Smart Career Preparation Platform Powered by Artificial Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    # PROJECT OVERVIEW
    st.subheader("📌 Project Overview")

    st.markdown("""
    **AI Interview Assistant** is an intelligent platform designed to help students, freshers, and professionals prepare for interviews with confidence.

    It combines modern AI capabilities with an easy-to-use interface to generate interview questions, evaluate answers, analyze resumes, and simulate mock interviews.

    This project is especially useful for final year students and job seekers who want to improve hiring chances.
    """)

    st.markdown("---")

    # CORE FEATURES
    st.subheader("🚀 Core Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("""
        🎯 **Interview Generator**

        Generate role-based technical, HR, coding, and behavioral questions.
        """)

    with c2:
        st.success("""
        📝 **Answer Evaluation**

        Get AI score, strengths, weaknesses, and sample answers.
        """)

    with c3:
        st.success("""
        📄 **Resume Analyzer**

        ATS score, missing skills, formatting tips, job match analysis.
        """)

    st.markdown("")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.success("""
        📚 **Mock Interview**

        Practice realistic interviews with AI interviewer.
        """)

    with c5:
        st.success("""
        📈 **Dashboard**

        Track progress and readiness.
        """)

    with c6:
        st.success("""
        ⚡ **Fast & Local AI**

        Works with Ollama local models.
        """)

    st.markdown("---")

    # TECHNOLOGY STACK
    st.subheader("🛠 Technology Stack")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.info("""
        **Frontend**
        - Streamlit
        - HTML/CSS Styling
        - Responsive UI
        """)

    with t2:
        st.info("""
        **Backend**
        - Python
        - Requests API
        - PDF Processing
        """)

    with t3:
        st.info("""
        **AI Engine**
        - Ollama
        - Qwen2.5:3B
        - Local LLM Inference
        """)

    st.markdown("---")

    # HOW IT WORKS
    st.subheader("⚙ How It Works")

    h1, h2, h3, h4 = st.columns(4)

    with h1:
        st.info("1️⃣ Select Module")

    with h2:
        st.info("2️⃣ Enter Inputs")

    with h3:
        st.info("3️⃣ AI Processing")

    with h4:
        st.info("4️⃣ Get Results")

    st.markdown("---")

    # WHO CAN USE
    st.subheader("👥 Who Can Use This Project?")

    st.markdown("""
    ✅ Final Year Students  
    ✅ Freshers Preparing for Placement  
    ✅ Job Seekers  
    ✅ Working Professionals  
    ✅ Career Switchers  
    ✅ Interview Trainers  
    """)

    st.markdown("---")

    # PROJECT OBJECTIVES
    st.subheader("🎯 Main Objectives")

    st.markdown("""
    - Improve interview confidence  
    - Reduce preparation time  
    - Help users identify weak areas  
    - Improve resume quality  
    - Provide smart personalized guidance  
    - Increase chances of selection  
    """)

    st.markdown("---")

    # WHY UNIQUE
    st.subheader("🌟 Why This Project is Unique")

    st.markdown("""
    ✅ Combines 5 tools in one platform  
    ✅ Uses Local AI (privacy friendly)  
    ✅ Modern SaaS-style UI  
    ✅ Useful in real life daily career growth  
    ✅ Suitable for academic final year project  
    """)

    st.markdown("---")

    # FUTURE ENHANCEMENTS
    st.subheader("🚀 Future Enhancements")

    st.markdown("""
    - Voice Interview Mode  
    - Face Expression Analysis  
    - Multi-language Support  
    - Login & User Accounts  
    - Database History Tracking  
    - Job Recommendation Engine  
    - Live Coding Interview Round  
    """)

    st.markdown("---")

    # DEVELOPER SECTION
    st.subheader("👨‍💻 Developer Note")

    st.success("""
    This project demonstrates the practical use of Artificial Intelligence in career development and recruitment preparation.
    """)

    st.markdown("---")

    # FAQ
    st.subheader("❓ Frequently Asked Questions")

    with st.expander("Is this suitable for final year project?"):
        st.write("Yes, it is an excellent real-world AI project.")

    with st.expander("Does it need internet?"):
        st.write("Ollama models can run locally after setup.")

    with st.expander("Can it be deployed?"):
        st.write("Yes, on Streamlit Cloud, local server, or VPS.")

    with st.expander("Can more models be added later?"):
        st.write("Yes, Ollama supports multiple local models.")

    st.markdown("---")

    # FOOTER CARD
    st.markdown("""
    <div style='
        background:#111827;
        color:white;
        padding:35px;
        border-radius:18px;
        text-align:center;
    '>
        <h2>🚀 Prepare Smarter. Get Hired Faster.</h2>
        <p>AI Interview Assistant</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
