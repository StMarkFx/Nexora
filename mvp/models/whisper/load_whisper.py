# load_whisper.py
import whisper

def download_whisper_model(model_size="base", model_dir="models/whisper"):
    """
    Downloads the Whisper model and saves it to the specified directory.
    
    Args:
        model_size (str): The size of the Whisper model (e.g., "base", "small", "medium").
        model_dir (str): The directory to save the model files.
    """
    print(f"Downloading Whisper {model_size} model...")
    model = whisper.load_model(model_size, download_root=model_dir)
    print(f"Whisper {model_size} model downloaded and saved to {model_dir}.")

if __name__ == "__main__":
    # Download the base Whisper model
    download_whisper_model(model_size="base")