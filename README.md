# <img src="/assests/icon.png" alt="Icon" width="30" height="30"> AI Resume Analyzer

**AI Resume Analyzer** is a Streamlit web app that analyzes uploaded resumes against a given job description using Google's Generative AI model.  
It provides matching probability, missing skills, project improvement suggestions, and final recommendations.

---

## 🚀 Features
- Upload your resume (PDF format).
- Paste the job description.
- Get an AI-powered analysis:
  - Matching probability (%)
  - Missing or related skills
  - Project feedback and suggestions
  - Resume improvement tips
- Download the analysis as a `.txt` file.

---

## 🎥 Demo

![Demo Video](https://github.com/user-attachments/assets/0b613a7e-b64f-4cb8-816b-8152294ff224)

---

## 📄 Requirements
- Python 3.8+
- Streamlit
- pdfplumber
- python-dotenv
- google-generativeai

(Install all from `requirements.txt`.)

---

## ⚡ Notes
- App uses **Google Gemini API** (`gemma-3-12b-it`) for generating insights.
- Make sure your `.env` file is correctly configured.

---