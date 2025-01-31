import streamlit as st
from src.core.assistant import Assistant

st.title("Nexora Voice Assistant")
assistant = Assistant()

user_input = st.text_input("Speak or type your command:")
if user_input:
    response = assistant.process_command(user_input)
    st.write(f"Response: {response}")
    assistant.tts.speak(response)