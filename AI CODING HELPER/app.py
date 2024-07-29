import streamlit as st
from gemini_client import get_suggestion

# Streamlit app title
st.title("AI Coding Helper")

# Text area for code input
code_input = st.text_area("Enter your code here:")

# Button to get suggestion
if st.button("Get Suggestion"):
    if code_input:
        # Get suggestion from Gemini API
        suggestion = get_suggestion(code_input)
        st.subheader("AI Suggestion")
        st.write(suggestion)
    else:
        st.error("Please enter some code to get a suggestion.")
