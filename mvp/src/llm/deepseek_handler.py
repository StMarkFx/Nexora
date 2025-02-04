import ollama

class DeepSeekHandler:
    def __init__(self, model_name="deepseek-r1-1.5b"):
        self.model_name = model_name

    def generate_response(self, prompt):
        response = ollama.generate(model=self.model_name, prompt=prompt)
        return response["response"]