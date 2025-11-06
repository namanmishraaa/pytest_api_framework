# Objective:
Generate a **complete, production-ready API automation testing framework** using **Pytest + Requests**, designed for **scalability, reusability, and CI/CD integration**.  
The framework must follow **clean architecture**, **solid design principles**, and **enterprise automation standards**.

---

# 🧱 Expected Folder Structure
```markdown

automation_framework/
├── tests/              # Contains all test cases
│   └── test_sample.py  # Example test file
├── config/             # Environment configs or constants
├── utils/              # Helper functions and utilities
├── fixtures/           # Shared pytest fixtures
├── reports/            # Test execution reports
├── conftest.py         # Global fixtures and hooks
├── requirements.txt    # Project dependencies
└── README.md           # Documentation

```


---

#  Framework Requirements

1. **Language & Libraries**
   - Python 3.10+
   - `pytest` for test runner
   - `requests` for API handling
   - `PyYAML` for configuration
   - `pytest-html` or `allure-pytest` for reporting
   - `loguru` or built-in `logging` for logs
   - `jsonschema` for response validation

2. **Core Architecture & Design**
   - Centralized `APIClient` class for all HTTP methods.
   - Environment-based configuration via `config.yaml`.
   - Configurable headers, base URLs, authentication tokens.
   - `BaseAPI` class encapsulating reusable request logic and assertions.
   - Layered approach:
     - `core/` → Framework logic (APIClient, assertions, utils)
     - `tests/` → Actual test cases
     - `data/` → Payloads & test data
     - `config/` → Environment, logger, and settings
   - Implement **SOLID** and **DRY** principles.

3. **Functional Requirements**
   - API client supporting GET, POST, PUT, DELETE.
   - Automatic token handling for authenticated APIs.
   - JSON schema validation for responses.
   - Parameterized tests using Pytest.
   - Hooks for setup/teardown and fixtures.
   - Retry mechanism for transient failures.
   - Parallel execution support (`pytest-xdist`).

4. **Reporting & Logs**
   - Generate Allure or HTML test reports.
   - Log every request and response with timestamp, status, and payload.
   - Save failed response payloads for debugging.
   - Screenshot equivalent for APIs (JSON dump on failure).

5. **Maintainability**
   - Fully modular and extensible.
   - Easy addition of new endpoints and tests.
   - Type hinting and docstrings for maintainability.
   - Clean, readable, and standardized naming conventions.
   - CI/CD ready (GitHub Actions / Jenkins / GitLab).

---

# Example Reference Snippets for Copilot

## config/environment_manager.py
```python
import yaml
import os

class EnvironmentManager:
    """Loads environment-specific configurations."""
    def __init__(self, env: str = None):
        env = env or os.getenv("TEST_ENV", "dev")
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        self.env_config = config[env]

    @property
    def base_url(self):
        return self.env_config["base_url"]

    @property
    def auth_token(self):
        return self.env_config.get("auth_token")
```

## core/api_client.py
```python
import requests
from loguru import logger

class APIClient:
    """Wrapper around requests with logging and error handling."""
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"{method.upper()} {url}")
        response = requests.request(method, url, headers=self._headers(), **kwargs)
        logger.info(f"Response [{response.status_code}]: {response.text}")
        response.raise_for_status()
        return response

    def get(self, endpoint, **kwargs): return self.request("get", endpoint, **kwargs)
    def post(self, endpoint, **kwargs): return self.request("post", endpoint, **kwargs)
    def put(self, endpoint, **kwargs): return self.request("put", endpoint, **kwargs)
    def delete(self, endpoint, **kwargs): return self.request("delete", endpoint, **kwargs)

```

## tests/conftest.py
```python
import pytest
from config.environment_manager import EnvironmentManager
from core.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    env = EnvironmentManager()
    return APIClient(base_url=env.base_url, token=env.auth_token)


```
## tests/test_user_endpoints.py
```python
import pytest

@pytest.mark.api
def test_get_user_details(api_client):
    response = api_client.get("/users/1")
    json_data = response.json()

    assert response.status_code == 200
    assert "username" in json_data
    assert json_data["id"] == 1
```
