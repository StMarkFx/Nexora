# Nexora Voice Assistant 🎙️

Nexora is a **voice-controlled AI assistant** that can browse files, summarize text, answer questions, and even control apps. Built with **DeepSeek** (local LLM), **Whisper** (speech-to-text), and **Coqui TTS** (text-to-speech), Nexora is like having your own Jarvis!


## Features ✨

- **Voice Interaction**: Speak commands and get voice responses.
- **Text Processing**: Answer questions, summarize text, and execute commands using **DeepSeek**.
- **API Integrations**:
  - **NewsAPI**: Fetch news headlines.
  - **OpenWeatherMap**: Get weather updates.
  - **Google Calendar**: Manage reminders and events.
- **Browser Automation**: Perform web searches and automate tasks using **Selenium/Playwright**.
- **Advanced Features**:
  - Reminders and alarms.
  - Email integration (Gmail API).
  - System monitoring (CPU, RAM usage).


## Tech Stack 🛠️

- **LLM**: DeepSeek (local)
- **Speech-to-Text**: OpenAI Whisper
- **Text-to-Speech**: Coqui TTS
- **APIs**: NewsAPI, OpenWeatherMap, Google Calendar API
- **Browser Automation**: Selenium/Playwright
- **Programming Language**: Python
- **Web Interface**: Streamlit


## Installation 🚀

### Prerequisites
- Python 3.8 or higher
- Microphone (for voice input)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nexora-voice-assistant.git
   cd nexora-voice-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up models:
   - **DeepSeek**: Place model files in `models/deepseek/`.
   - **Whisper**: Place model files in `models/whisper/`.
   - **Coqui TTS**: Place model files in `models/coqui_tts/`.

4. Configure API keys:
   - Create a `config/api_keys.json` file:
     ```json
     {
       "newsapi": "YOUR_NEWSAPI_KEY",
       "openweathermap": "YOUR_OPENWEATHERMAP_KEY",
       "google_calendar": "YOUR_GOOGLE_CALENDAR_CREDENTIALS"
     }
     ```

---

## Usage 🎯

### Running the Assistant
1. Start the Streamlit interface:
   ```bash
   streamlit run main.py
   ```

2. Use the interface:
   - Click **"Record Voice Command"** to speak your command.
   - Wait for Nexora to process your command and respond.

### Example Commands
- **Weather**: "What’s the weather in New York?"
- **News**: "What are the latest news headlines?"
- **Reminders**: "Remind me to call John at 3 PM."
- **Web Search**: "Search for AI news on Google."


## Project Structure 📂
```
nexora-voice-assistant/
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── main.py                         # Entry point for the voice assistant (Streamlit)
├── config/                         # Configuration files
│   ├── api_keys.json               # Store API keys securely
│   └── settings.json               # User preferences and settings
├── models/                         # Local models (DeepSeek, Whisper, Coqui TTS)
│   ├── deepseek/                   # DeepSeek model files
│   ├── whisper/                    # Whisper model files
│   └── coqui_tts/                  # Coqui TTS model files
├── src/                            # Source code
│   ├── stt/                        # Speech-to-text module
│   ├── tts/                        # Text-to-speech module
│   ├── llm/                        # Language model module
│   ├── api/                        # API integrations
│   ├── browser/                    # Browser automation
│   ├── utils/                      # Utility functions
│   └── core/                       # Core functionality
├── tests/                          # Unit and integration tests
├── logs/                           # Log files for debugging
├── assets/                         # Static assets (icons, sounds)
└── scripts/                        # Helper scripts (setup, deployment)
```


## Error Handling 🛑

Nexora includes **robust error handling** for:
- **No speech detected** during recording.
- **API failures** (e.g., Weather API or News API is down).
- **Invalid user commands**.
- **File I/O errors** (e.g., unable to save or read audio files).
- **Microphone access issues**.


## Contributing 🤝

Contributions are welcome! Here’s how you can help:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.


## License 📜

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


## Acknowledgments 🙏

- **DeepSeek**: For the local LLM.
- **OpenAI Whisper**: For speech-to-text.
- **Coqui TTS**: For text-to-speech.
- **Streamlit**: For the web interface.


## Contact 📧

For questions or feedback, reach out to:
- **Name**: [St. Mark Adebayo](your.email@example.com)
- **LinkedIn**: [St. Mark Adebayo](https://www.linkedin.com/in/stmarkadebayo)
- **GitHub**: [yourusername](https://github.com/yourusername)

