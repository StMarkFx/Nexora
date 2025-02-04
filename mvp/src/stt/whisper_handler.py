import whisper

class WhisperHandler:
    def __init__(self, model_path="models/whisper/base.pt"):
        self.model = whisper.load_model(model_path)

    def transcribe(self, audio_file):
        result = self.model.transcribe(audio_file)
        return result["text"]