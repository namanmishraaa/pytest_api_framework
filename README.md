# 🧪 Pytest Automation Framework


A simple and scalable **Pytest-based automation framework** designed for learning and professional use.

---

## 📂 Project Structure

```markdown

automation_framework/
├── config/
│   └── config.yaml
│
├── fixtures/
│   └── auth_fixture.py
│
├── tests/
│   ├── test_auth.py
│
├── utils/
│   ├── config_reader.py
│
├── reports/                         
│
├── conftest.py
├── requirements.txt
└── README.md                        


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

