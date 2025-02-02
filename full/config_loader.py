import json
import yaml
import logging
import os

# Load logging configuration
def setup_logging(default_path='logging_config.yaml', default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()
logger = logging.getLogger(__name__)

# Load API keys
def load_api_keys(file_path='config/api_keys.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error loading API keys: {e}")
        return {}

# Load settings
def load_settings(file_path='config/settings.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error loading settings: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    api_keys = load_api_keys()
    settings = load_settings()
    logger.info(f"Loaded settings: {settings}")
