# Techin510-Lab6_HW
# README File
Streamlit AI Assistant
This Streamlit app serves as an AI assistant that allows users to upload files and generate song lyrics using OpenAI. Users can interact with the assistant through a chat-like interface.

Features
File Upload: Users can upload files (e.g., text files, CSV files) to the app.
Chat Input: Users can type messages to interact with the AI assistant.
Lyrics Generation: The assistant uses OpenAI Codex to generate song lyrics based on user input.
Getting Started
Installation:
Make sure you have Python and Streamlit and OpenAI installed.
import streamlit as st
import openai
import os

Set the OpenAI API key in the  .env file 
Run the app:
streamlit run app.py

Usage:
Upload a file using the file uploader.
Type messages in the chat input.
Click “Generate Lyrics” to receive AI-generated lyrics.
Example
Here’s how the app works:

Upload a file (e.g., a text file 'janiesGotAGun.txt' with Aerosmith's song lyrics).
Chat with the AI assistant.
"write another song with similar lyrics" is the recommended prompt.
Click “Generate Lyrics” to create new song lyrics.
Acknowledgments
This app uses Streamlit for the user interface.
Lyrics generation is powered by OpenAI.

Learning and Issues: The bot generates new lyrics exhibiting the implementation of the RAG feature. However sometimes, it generates only 4 lines lyrics and most times, it generates a full song.  