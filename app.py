import streamlit as st
from resumeParser import extract_text
from jobParser import clean_description
from matcher import extract_keywords, calculate_match_score

# Title
st.set_page_config(page_title="AI Resume Matcher", layout="centered")
st.title("🤖 AI Resume Screener & Job Matcher")

# Upload Resume
st.subheader("📄 Upload Your Resume")
uploaded_file = st.file_uploader("Upload DOCX resume", type=["docx"])

# Job Description Input
st.subheader("📝 Paste Job Description")
job_description = st.text_area("Paste the job description here", height=200)

# Process
if st.button("🔍 Match Now") and uploaded_file and job_description:
    with st.spinner("Processing..."):

        # Step 1: Read resume
        resume_text = extract_text(uploaded_file)

        # Step 2: Clean job description
        job_cleaned = clean_description(job_description)

        # Step 3: Extract keywords
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_cleaned)

        # Step 4: Match score
        match_score = calculate_match_score(" ".join(resume_keywords), " ".join(job_keywords))

        # Step 5: Show Results
        st.success(f"✅ Match Score: {match_score}%")

        # Missing keywords
        missing = list(set(job_keywords) - set(resume_keywords))
        if missing:
            st.warning("🔍 You may want to add these missing skills/keywords:")
            st.write(", ".join(sorted(missing)))
        else:
            st.info("✅ Your resume covers most job keywords!")

# Footer
st.markdown("---")
st.markdown("Created by [Ali Husain] | Powered by Python & NLP")