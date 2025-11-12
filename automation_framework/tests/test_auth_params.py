# This file contains parametrized tests for authentication using pytest and reads test data from a YAML file.
import pytest
from utils.data_reader import load_test_data
from utils.config_reader import get_base_url, get_credentials
import requests
from utils.logger import logger

test_data = load_test_data('auth_data.yaml')
@pytest.mark.parametrize('TestCredentials', [
    test_data['valid_credentials'],
    test_data['invalid_credentials'],
    test_data['invalid_credentials'],
])
def test_auth_token_param(TestCredentials):
    logger.info(f"Starting test_auth_token_param with credentials: {TestCredentials['username']}")
    base_url = get_base_url()
    credentials = {
        "username": TestCredentials['username'],
        "password": TestCredentials['password']
    }
    logger.debug(f"Attempting authentication with username: {credentials['username']}")
    response = requests.post(f"{base_url}/auth", json=credentials)
    logger.info(f"Received response with status code: {response.status_code}")
    logger.debug(f"Response body: {response.text}")

    if TestCredentials['username'] == 'admin' :
        assert response.status_code == 200
        assert 'token' in response.json(), "Expected token not found"
        logger.info("Authentication successful for valid credentials.")
    else:
        assert 'token' not in response.json(), "Token should not be present for invalid credentials"
        logger.info("Authentication failed as expected for invalid credentials.")
    logger.info("Finished test_auth_token_param")