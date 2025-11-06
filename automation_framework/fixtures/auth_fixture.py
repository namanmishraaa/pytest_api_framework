import pytest
import requests
from utils.config_reader import read_config


@pytest.fixture(scope="session", autouse=True)
def setup_environment(env):
    """Sets up the testing environment based on the provided environment option."""
    print("Setting up the testing environment...")
    yield
    print("Tearing down the testing environment...")
    # Additional setup can be done here if needed

@pytest.fixture(scope="session")
def get_token(setup_environment):
    """Creates and returns a session-wide token for authentication."""
    config = read_config()
    base_url = config["base_url"]
    payload = {
        "username": config["username"],
        "password": config["password"]
    }

    response = requests.post(f"{base_url}/auth", json=payload)
    assert response.status_code == 200, f"Auth failed: {response.text}"
    token = response.json().get("token")

    # yield instead of return → allows teardown if needed
    yield token
