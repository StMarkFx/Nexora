from src.stt.whisper_handler import WhisperHandler
from src.tts.coqui_tts_handler import CoquiTTSHandler
from src.llm.deepseek_handler import DeepSeekHandler
from src.api.weather_api import WeatherAPI
from src.api.news_api import NewsAPI
from src.api.calendar_api import CalendarAPI

class Assistant:
    def __init__(self):
        # Initialize all modules
        self.stt = WhisperHandler()  # Speech-to-text
        self.tts = CoquiTTSHandler()  # Text-to-speech
        self.llm = DeepSeekHandler()  # Language model
        self.weather_api = WeatherAPI()  # Weather API
        self.news_api = NewsAPI()  # News API
        self.calendar_api = CalendarAPI()  # Calendar API

    def process_command(self, command):
        # Handle weather queries
        if "weather" in command:
            city = command.split("weather in ")[1]
            return self.weather_api.get_weather(city)
        
        # Handle news queries
        elif "news" in command:
            return self.news_api.get_news()
        
        # Handle calendar queries
        elif "remind" in command or "calendar" in command:
            return self.calendar_api.add_event(command)
        
        # Handle general queries
        else:
            return self.llm.generate_response(command)

    def run(self):
        # Main loop for the assistant
        while True:
            audio_file = "user_input.wav"  # Record audio and save to this file
            command = self.stt.transcribe(audio_file)  # Convert speech to text
            response = self.process_command(command)  # Process the command
            self.tts.speak(response)  # Generate voice response