from src.stt.whisper_handler import WhisperHandler
from src.tts.coqui_tts_handler import CoquiTTSHandler
from src.llm.deepseek_handler import DeepSeekHandler
from src.api.weather_api import WeatherAPI

class Assistant:
    def __init__(self):
        self.stt = WhisperHandler()
        self.tts = CoquiTTSHandler()
        self.llm = DeepSeekHandler()
        self.weather_api = WeatherAPI()

    def process_command(self, command):
        if "weather" in command:
            city = command.split("weather in ")[1]
            return self.weather_api.get_weather(city)
        else:
            return self.llm.generate_response(command)

    def run(self):
        while True:
            audio_file = "user_input.wav"  # Record audio and save to this file
            command = self.stt.transcribe(audio_file)
            response = self.process_command(command)
            self.tts.speak(response)