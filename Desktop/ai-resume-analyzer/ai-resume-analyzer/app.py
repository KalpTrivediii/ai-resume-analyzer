import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from analyzer import analyze_resume
import pypdf2
import re

# Page config
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# Title + Tagline (STEP 5 ✅)
st.title("🚀 AI Resume Analyzer")
st.caption("Upload your resume and compare with a job description")
st.markdown("### 🎯 Get instant feedback like a UK recruiter")

# Button styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Upload PDF
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type="pdf")

# Job description input
job = st.text_area("💼 Paste job description")

# Extract text function
def extract_text_from_pdf(file):
    pdf_reader = pypdf2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

# Button
if st.button("Analyze"):
    if uploaded_file and job:
        with st.spinner("🔍 AI is analyzing your resume..."):  # STEP 4 ✅
            resume_text = extract_text_from_pdf(uploaded_file)

            # Debug (optional)
            st.write("Resume length:", len(resume_text))

            result = analyze_resume(resume_text, job)

            st.success("✅ Analysis Complete!")
            st.markdown("## 📊 Analysis Result")

            # Extract score
            score_match = re.search(r"(\d+)", result)
            score = int(score_match.group(1)) if score_match else 50

            # Show score nicely
            st.metric("Match Score", f"{score}%")
            st.progress(score / 100)

            st.markdown("---")
            st.markdown(result)

    else:
        st.warning("⚠️ Please upload resume and enter job description")