import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Import our data contract from schemas.py
from app.schemas import FullDeaCertificateSchema

# 1. Load environment variables from your local hidden .env file
load_dotenv()

# 2. Initialize the Gemini API client safely
# The SDK automatically finds your GEMINI_API_KEY from the loaded environment
client = genai.Client()

def extract_dea_certificate(file_path: str):
    with open(file_path, "rb") as file:
        file_bytes = file.read()
        mime_type: str = "application/pdf"
        
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=FullDeaCertificateSchema,
    )
    
    # 3. This functions exactly the same way as before
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(data=file_bytes, mime_type=mime_type),
            "Extract all relevant information from this DEA certificate."
        ],
        config=config
    )
    return response.parsed

if __name__ == "__main__":
    sample_file = "sample_dea_certificate.pdf"
    
    if os.path.exists(sample_file):
        print(f"Processing {sample_file}...")
        result = extract_dea_certificate(sample_file)
        
        print("\n--- Extracted DEA Certificate Data ---")
        print(f"DEA Number: {result.dea_number}")
        print(f"Registrant Name: {result.registrant_name}")
        print(f"Business Activity: {result.business_activity}")
        print(f"Schedules: {result.schedules}")
        print(f"Expiration Date: {result.expiration_date}")
    else:
        print(f"Please place a test file at '{sample_file}' to run a test extraction.")
