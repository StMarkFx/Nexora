import ollama

class DeepSeekChatbot:
    def __init__(self):
        self.model_name = "deepseek-r1:1.5b"  # Ensure this matches your Ollama model

    def get_response(self, query: str) -> str:
        response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": query}])
        return response['message']

if __name__ == "__main__":
    bot = DeepSeekChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = bot.get_response(user_input)
        print("Nexora:", response)
