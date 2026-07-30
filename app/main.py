import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Import our data contract from schemas.py
from app.schemas import FullDeaCertificateSchema

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini API client
client = genai.Client(api_key=os.getenv("REDACTED_GEMINI_API_KEY"))

# 🔗 STEP 1: Define the structured rules using your imported schema
config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=FullDeaCertificateSchema, # Uses your imported data contract
)
