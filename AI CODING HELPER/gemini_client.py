import google.generativeai as genai
import os

# Set the API key directly for simplicity
API_KEY = "AIzaSyDRDD-9HZWdu8gSxPf2ZqfDe_MzqijI5fM"
genai.configure(api_key=API_KEY)

def get_suggestion(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate(prompt=prompt, max_tokens=50)

        print("API Response:", response)  # Debug line

        if "choices" in response and len(response["choices"]) > 0:
            return response["choices"][0].get("text", "No suggestion available")
        else:
            return "Unexpected response format"
    except Exception as e:
        print(f"Request error: {e}")
        return "Error fetching suggestion"
