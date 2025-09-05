import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Set your GEMINI_API_KEY in a .env file!")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Prompt
prompt = "Generate 5 detailed test cases for login functionality with inputs and expected outputs."

# Generate response
response = model.generate_content(prompt)

# Print
print(response.text)
    