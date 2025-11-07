# 🤖 GEMINI Analysis

This document provides a comprehensive overview of the project in this directory, to be used as instructional context for future interactions.

---

## 📝 Project Overview

This project is a UI automation testing framework for the [SauceDemo](https://www.saucedemo.com/) website. It is built with Python and leverages several popular testing libraries and design patterns:

- **Core Technology:** Python
- **Browser Automation:** Playwright
- **Test Runner:** Pytest
- **Design Pattern:** Page Object Model (POM)

The framework is organized into a `saucedemo_automation` directory, which contains the page objects, test scripts, and utility files. The project also includes documentation files (`UI_Documentation.md` and `copilot_prompt_framework_blueprint.md`) that describe the framework and its intended architecture.

---

## 🚀 Building and Running

Here are the key commands for setting up and running the tests:

### 1. Install Dependencies

```bash
# Install Python packages
pip install -r saucedemo_automation/requirements.txt

# Install Playwright browsers
playwright install
```

### 2. Run Tests

```bash
# Run all tests
pytest saucedemo_automation/tests/

# Run with a specific browser (e.g., chromium)
pytest saucedemo_automation/tests/ --browser chromium

# Run in headless mode
pytest saucedemo_automation/tests/ --browser chromium --headless
```

---

## 🧱 Development Conventions

The project follows a set of conventions to ensure code quality and maintainability:

- **Page Object Model (POM):** Each page of the application has its own corresponding class in the `saucedemo_automation/pages` directory.
- **Separation of Concerns:** Test logic is strictly separated from page interaction logic. Tests reside in `saucedemo_automation/tests`, while page objects are in `saucedemo_automation/pages`.
- **Naming Conventions:**
  - Test functions are named using a `test_<action>_<expected>()` pattern (e.g., `test_valid_login()`).
  - Page object methods use a `verb_noun()` pattern (e.g., `click_login()`).
- **Assertions:** All assertions (`assert` statements) are performed within the test files, not in the page object files.
- **Locators:** Element locators are defined as private class attributes within their respective page object classes (e.g., `_USERNAME_INPUT`).
