import streamlit as st
import sounddevice as sd
import soundfile as sf
import numpy as np
from src.core.assistant import Assistant

# Initialize the assistant
assistant = Assistant()

# Streamlit UI
st.title("Nexora Voice Assistant")
st.write("Welcome to Nexora! Click the button below to speak your command.")

# Record audio button
if st.button("Record Voice Command"):
    st.write("Recording... Speak now!")
    
    try:
        # Record audio
        sample_rate = 16000  # 16 kHz sample rate
        duration = 5  # 5 seconds recording
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()  # Wait for recording to finish
        
        # Save audio to file
        audio_file = "user_input.wav"
        sf.write(audio_file, audio, sample_rate)
        st.write("Recording complete! Processing your command...")

        # Process the audio file
        try:
            command = assistant.stt.transcribe(audio_file)
            if not command.strip():  # Check if the command is empty
                st.error("No speech detected. Please try again.")
            else:
                st.write(f"You said: {command}")

                # Generate response
                try:
                    response = assistant.process_command(command)
                    st.write(f"Response: {response}")

                    # Generate voice response
                    try:
                        assistant.tts.speak(response)
                        st.audio("output.wav", format="audio/wav")
                    except Exception as tts_error:
                        st.error(f"Failed to generate voice response: {tts_error}")
                except Exception as process_error:
                    st.error(f"Failed to process command: {process_error}")
        except Exception as stt_error:
            st.error(f"Failed to transcribe audio: {stt_error}")
    except sd.PortAudioError as pa_error:
        st.error(f"Microphone access error: {pa_error}. Please check your microphone settings.")
    except Exception as record_error:
        st.error(f"Recording failed: {record_error}")