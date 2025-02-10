import torch
from TTS.api import TTS

class CoquiTTS:
    def __init__(self):
        self.tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")  # Change model if needed

    def speak(self, text):
        self.tts.tts_to_file(text=text, file_path="output.wav")
        print("Speech generated: output.wav")

if __name__ == "__main__":
    tts = CoquiTTS()
    tts.speak("Hello, I am Nexora!")
