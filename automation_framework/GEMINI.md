# Gemini Project Context: Pytest API Automation Framework

## Project Overview

This project is a Python-based API automation testing framework designed for scalability, reusability, and CI/CD integration. It uses `pytest` as the test runner and `requests` for making API calls. The framework is designed to test a booking API.

The framework follows a clean architecture with a clear separation of concerns:
*   **`config/`**: Contains environment-specific configurations, such as base URLs and credentials.
*   **`fixtures/`**: Holds reusable pytest fixtures, such as authentication tokens.
*   **`logs/`**: Stores detailed execution logs for each test run.
*   **`reports/`**: Contains the generated HTML test reports.
*   **`tests/`**: Includes the actual test cases.
*   **`utils/`**: Provides utility functions, such as a configuration reader and a logger.

## Building and Running

### Dependencies

The project dependencies are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
```

### Running Tests

To run the tests, execute the following command in the root directory:

```bash
pytest
```

This will run all the tests and generate an HTML report in the `reports/` directory and a log file in the `logs/` directory.

## Development Conventions

*   **Testing**: The framework uses `pytest` for writing and running tests. Tests are organized in the `tests/` directory. Test functions should start with `test_`.
*   **Configuration**: Environment-specific configurations are stored in `config/config.yaml`. The `utils/config_reader.py` module provides a utility to read the configuration.
*   **Logging**: The framework uses the built-in `logging` module for logging. A centralized logger is configured in `utils/logger.py`.
*   **Reporting**: `pytest-html` is used to generate HTML reports. The report is generated at `reports/report.html`.
*   **Fixtures**: Reusable fixtures are defined in `fixtures/` and `conftest.py`.
*   **Code Style**: The code should follow standard Python conventions (PEP 8).
