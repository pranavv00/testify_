import streamlit as st
import google.generativeai as genai

# Configure Gemini API from Streamlit secrets (set in Streamlit Cloud)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# App title
st.title("🚀 Testify – AI-Powered Test Case Generator")
st.caption("Transforming requirements into test cases instantly")

# Input field
feature_description = st.text_area("📝 Enter feature/requirement description:")

# Generate button
if st.button("Generate Test Cases"):
    if feature_description.strip():
        # Use a valid Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            f"Generate detailed software test cases (functional + edge cases + negative cases) for: {feature_description}"
        )

        st.subheader("✅ Generated Test Cases")
        st.write(response.text)
    else:
        st.warning("Please enter a feature description first.")
