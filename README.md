# 🧪 Pytest Automation Framework


A simple and scalable **Pytest-based automation framework** designed for learning and professional use.

---

## 📂 Project Structure

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



## ⚙️ Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
````
---


## 🧩 Run Tests
---
```
pytest -v               # Run all tests
pytest -k "sample"      # Run specific tests
pytest -v --maxfail=1   # Stop after first failure
```

---

## ✅ Example Test

```
# tests/test_sample.py
def test_sample():
    assert 2 + 2 == 4
```

