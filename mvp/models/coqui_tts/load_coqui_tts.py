# load_coqui_tts.py
from TTS.api import TTS

def download_coqui_tts_model(model_name="tts_models/en/ljspeech/tacotron2-DDC", model_dir="models/coqui_tts"):
    """
    Downloads the Coqui TTS model and saves it to the specified directory.
    
    Args:
        model_name (str): The name of the Coqui TTS model.
        model_dir (str): The directory to save the model files.
    """
    print(f"Downloading Coqui TTS model: {model_name}...")
    tts = TTS(model_name=model_name, progress_bar=False, gpu=False)
    print(f"Coqui TTS model downloaded and saved to {model_dir}.")

if __name__ == "__main__":
    # Download the Tacotron2-DDC model
    download_coqui_tts_model(model_name="tts_models/en/ljspeech/tacotron2-DDC")