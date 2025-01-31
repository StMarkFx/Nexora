from transformers import pipeline

class DeepSeekHandler:
    def __init__(self, model_path="models/deepseek/"):
        self.generator = pipeline('text-generation', model=model_path)

    def generate_response(self, prompt):
        response = self.generator(prompt, max_length=50)
        return response[0]['generated_text']