from TTS.api import TTS

class CoquiTTSHandler:
    def __init__(self, model_path="models/coqui_tts/tacotron2-DDC"):
        self.tts = TTS(model_name=model_path, progress_bar=False, gpu=False)

    def speak(self, text, output_file="output.wav"):
        self.tts.tts_to_file(text=text, file_path=output_file)