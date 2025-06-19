import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_caption(description):
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate_content(f"Write an Instagram caption for: {description}")
    return response.text
