import streamlit as st
import pdfplumber
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

st.set_page_config(page_title='AI Resume Analyzer', page_icon='assests/icon.png',layout='wide')

st.title("AI Resume Analyzer")



def insights(content,job_des):
    model = genai.GenerativeModel(model_name="gemma-3-12b-it")  
    prompt = f"""
    You are an expert career consultant and hiring manager.
    Analyze the following two inputs carefully:

    Resume Text:
    {content}

    Job Description:
    {job_des}

    Your tasks:

    First, calculate the probability (0% to 100%) of how well the resume matches the job description.

    Then, give a detailed analysis covering:

    Skills: 
    List important skills required in the Job Description.
    For each required skill:
    Check if it is exactly present in the resume.
    If not exactly present, check if a similar or related skill is present.
    If missing or only partially matched, clearly point it out.

    Projects: 
    Identify and review all projects mentioned in the resume.
    For each project:
    Analyze if the project description is well-written:
    Does it clearly explain what was built?
    Does it mention tools, technologies, results, and impact?
    If not, suggest exactly how the project description should be improved.
    Check if the project is aligned with the job role:
    If a project is unrelated, suggest either:
    A new relevant project idea.
    Or a way to reframe the project description to highlight transferable skills.

    Improvements:
    How can the candidate rewrite or improve their project descriptions to align better with the job?
    Mention specific keywords that should appear in the resume to improve matching (short).

    Final Recommendation: Summarize whether the candidate should apply now, or first improve their resume in one short paragraph.

    Output format:
    Matching Probability: __%
    Missing Skills: (if any otherwise not)
    Suggested Projects: (if any otherwise not)
    Resume Improvement Tips:
    Final Recommendation:
    """
    response = model.generate_content(prompt)
    return response.text.strip()
def main():
    uploaded_resume = st.file_uploader("Upload Your Resume (pdf)",type=['pdf'])
    if uploaded_resume is not None:
        st.session_state['resume_file'] = uploaded_resume

    content = ''
    if 'resume_file' in st.session_state:
        with pdfplumber.open(st.session_state['resume_file']) as resume:
            content = "".join([page.extract_text() for page in resume.pages])


    job_description = st.text_area("Paste the Job Description here:")
    if job_description is not None:
        st.session_state['job_description'] = job_description

    if 'job_description' in st.session_state:
        job_des = st.session_state['job_description']

    if 'ai_insights' not in st.session_state:
        st.session_state.ai_insights = ''
    
    analyzed_button = st.button("Start Analysis")
    if analyzed_button and uploaded_resume and job_description:
        with st.spinner("Analysis..."):
            st.session_state.ai_insights = insights(content,job_des)
    
    if st.session_state.ai_insights:
        st.subheader("AI Analysis")
        st.write(st.session_state.ai_insights)
        
        st.download_button(
            label='Download Your Analysis',
            data=st.session_state.ai_insights,
            file_name='resume_analysis.txt',
            mime='text/plain'
        )



if __name__=="__main__":
    main()