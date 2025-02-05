import streamlit as st
import sounddevice as sd
import soundfile as sf
from src.stt.whisper_handler import WhisperHandler
from src.tts.coqui_tts_handler import CoquiTTSHandler
from src.llm.deepseek_handler import DeepSeekHandler

# Initialize modules
stt = WhisperHandler()
tts = CoquiTTSHandler()
llm = DeepSeekHandler()

# Streamlit UI
st.title("Nexora MVP")
st.write("Click the button below to speak your command.")

if st.button("Record Voice Command"):
    st.write("Recording... Speak now!")
    
    # Record audio
    sample_rate = 16000  # 16 kHz sample rate
    duration = 5  # 5 seconds recording
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()  # Wait for recording to finish
    
    # Save audio to file
    audio_file = "user_input.wav"
    sf.write(audio_file, audio, sample_rate)
    st.write("Recording complete! Processing your command...")

    # Transcribe audio
    command = stt.transcribe(audio_file)
    st.write(f"You said: {command}")

    # Generate response using DeepSeek
    response = llm.generate_response(command)
    st.write(f"Response: {response}")

    # Generate voice response
    tts.speak(response)
    st.audio("output.wav", format="audio/wav")