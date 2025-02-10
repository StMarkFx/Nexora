from deepseek.chat import Chat  # Adjust import based on your installation

class DeepSeekChatbot:
    def __init__(self):
        self.chatbot = Chat(model="deepseek-chat")  # Load DeepSeek model

    def get_response(self, query: str) -> str:
        response = self.chatbot.ask(query)
        return response["message"]  # Adjust based on actual response format

if __name__ == "__main__":
    bot = DeepSeekChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = bot.get_response(user_input)
        print("Nexora:", response)
