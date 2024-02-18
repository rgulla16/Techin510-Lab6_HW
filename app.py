import streamlit as st
import openai
import os

from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize session state variables
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv"])

if uploaded_file:
    st.session_state.uploaded_file = uploaded_file

# Chat input
user_input = st.text_input("Chat with the AI assistant:")

if st.button("Generate Lyrics"):
    try:
        # Call the Chat Completions API with OpenAI Codex
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        generated_lyrics = response.choices[0].message["content"]
        st.write(f"Generated Lyrics:\n{generated_lyrics}")
    except Exception as e:
        st.error(f"Error generating lyrics: {e}")

# Display uploaded file (if any)
if st.session_state.uploaded_file:
    st.write(f"Uploaded file: {st.session_state.uploaded_file.name}")
