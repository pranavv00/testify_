import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# App title
st.title("🚀 Testify – AI-Powered Test Case Generator")
st.caption("Transforming requirements into test cases instantly")

# Input field
feature_description = st.text_area("📝 Enter feature/requirement description:")

# Generate button
if st.button("Generate Test Cases"):
    if feature_description.strip():
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Generate test cases for: {feature_description}")

        st.subheader("✅ Generated Test Cases")
        st.write(response.text)
    else:
        st.warning("Please enter a feature description first.")
