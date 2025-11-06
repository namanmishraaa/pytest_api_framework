import yaml
import os

def read_config():
    """Reads configuration YAML file and returns it as a dictionary."""
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yaml")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def get_base_url():
    return read_config().get("base_url")

def get_credentials():
    cfg = read_config()
    return {"username": cfg.get("username"), "password": cfg.get("password")}
