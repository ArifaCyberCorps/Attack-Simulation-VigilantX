import yaml
import logging

def load_config(file_path):
    """Loads a YAML configuration file."""
    try:
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
            return config
    except Exception as e:
        logging.error(f"Failed to load config at {file_path}: {e}")
        return {}