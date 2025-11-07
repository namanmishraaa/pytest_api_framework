import requests, pytest
from utils.config_reader import read_config, get_base_url

def test_read_config_returns_base_url():
    config = read_config()
    print(config)
    assert "base_url" in config
    assert get_base_url().startswith("https://")

@pytest.mark.negative_tests
def test_auth_with_invalid_credentials():
    config = read_config()
    base_url = config["base_url"]
    payload = {"username": "wrong", "password": "wrong"}
    response = requests.post(f"{base_url}/auth", json=payload)

    assert response.status_code == 200
    assert "token" not in response.json(), "Token should not be generated for invalid credentials"
