# 🧪 SauceDemo UI Automation Framework
**Tech Stack:** Python · Playwright · Pytest · Page Object Model (POM)  
**Application Under Test (AUT):** [https://www.saucedemo.com/](https://www.saucedemo.com/)

---

## 📘 1. Project Overview

This project automates end-to-end functional and UI testing for the [SauceDemo](https://www.saucedemo.com/) web application.

It follows the **Page Object Model (POM)** design pattern to ensure scalability, maintainability, and readability.  
The framework leverages **Playwright** for browser automation and **pytest** for test execution.

---

## 🏗️ 2. Framework Architecture

```plaintext
saucedemo-automation/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_info_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   ├── test_checkout.py
│
├── utils/
│   ├── config.py
│   ├── helpers.py
│
├── conftest.py
├── requirements.txt
└── UI_Documentation.md
````

**Key principles:**

* Each page in the application corresponds to one Page Object class.
* Each Page Object exposes **methods** that represent **user interactions**.
* Tests call these methods — never direct DOM locators.

---

## 🧭 3. Pages Overview

| Page Name              | File                        | Description                                        |
| ---------------------- | --------------------------- | -------------------------------------------------- |
| Login Page             | `login_page.py`             | Handles user login, invalid credential checks      |
| Products Page          | `products_page.py`          | Displays inventory items and “Add to Cart” actions |
| Cart Page              | `cart_page.py`              | Displays selected products                         |
| Checkout Info Page     | `checkout_info_page.py`     | Captures shipping details                          |
| Checkout Overview Page | `checkout_overview_page.py` | Shows final order summary                          |
| Checkout Complete Page | `checkout_complete_page.py` | Displays confirmation message                      |

---

## 🧩 4. Page-by-Page DOM Documentation

### 🟦 Login Page

**URL:** `/`
**Description:** First page for login access.

| Element        | Locator                    | Type     | Description                   |
| -------------- | -------------------------- | -------- | ----------------------------- |
| Username Input | `#user-name`               | `input`  | Username field                |
| Password Input | `#password`                | `input`  | Password field                |
| Login Button   | `#login-button`            | `button` | Triggers login action         |
| Error Message  | `.error-message-container` | `div`    | Displays invalid login errors |

**Methods:**

* `enter_username(username: str)`
* `enter_password(password: str)`
* `click_login()`
* `get_error_message() -> str`

---

### 🟩 Products Page

**URL:** `/inventory.html`
**Description:** Main dashboard of items available for purchase.

| Element            | Locator                | Type     | Description           |
| ------------------ | ---------------------- | -------- | --------------------- |
| Item Title         | `.inventory_item_name` | `a`      | Product link          |
| Add to Cart Button | `.btn_inventory`       | `button` | Adds product to cart  |
| Cart Icon          | `.shopping_cart_link`  | `a`      | Opens cart page       |
| Cart Badge         | `.shopping_cart_badge` | `span`   | Shows number of items |

**Methods:**

* `add_to_cart(item_name: str)`
* `open_cart()`
* `get_cart_count() -> int`

---

### 🟨 Cart Page

**URL:** `/cart.html`
**Description:** Displays items added to the shopping cart.

| Element         | Locator      | Type     | Description                |
| --------------- | ------------ | -------- | -------------------------- |
| Cart Items      | `.cart_item` | `div`    | Container for each product |
| Checkout Button | `#checkout`  | `button` | Proceeds to checkout page  |

**Methods:**

* `get_cart_items() -> list[str]`
* `click_checkout()`

---

### 🟧 Checkout: Your Information Page

**URL:** `/checkout-step-one.html`
**Description:** Captures user shipping details.

| Element         | Locator        | Type     | Description                |
| --------------- | -------------- | -------- | -------------------------- |
| First Name      | `#first-name`  | `input`  | Customer’s first name      |
| Last Name       | `#last-name`   | `input`  | Customer’s last name       |
| Postal Code     | `#postal-code` | `input`  | Customer’s postal code     |
| Continue Button | `#continue`    | `button` | Proceeds to order overview |

**Methods:**

* `fill_shipping_info(first, last, zip)`
* `click_continue()`

---

### 🟪 Checkout: Overview Page

**URL:** `/checkout-step-two.html`
**Description:** Displays final order summary and total price.

| Element       | Locator      | Type     | Description             |
| ------------- | ------------ | -------- | ----------------------- |
| Item Summary  | `.cart_item` | `div`    | Ordered product summary |
| Finish Button | `#finish`    | `button` | Completes the order     |

**Methods:**

* `review_order()`
* `click_finish()`

---

### 🟥 Checkout: Complete Page

**URL:** `/checkout-complete.html`
**Description:** Displays confirmation message after successful purchase.

| Element              | Locator             | Type     | Description                     |
| -------------------- | ------------------- | -------- | ------------------------------- |
| Confirmation Message | `.complete-header`  | `h2`     | "THANK YOU FOR YOUR ORDER" text |
| Back Home Button     | `#back-to-products` | `button` | Returns to product list         |

**Methods:**

* `get_confirmation_message() -> str`
* `click_back_home()`

---

## 🔄 5. Core Workflows

### ✅ Login Flow

1. Open login page
2. Enter username/password
3. Click login
4. Verify navigation to `/inventory.html`

### ✅ Add to Cart Flow

1. From Products Page, add item(s)
2. Open Cart Page
3. Validate cart badge count

### ✅ Checkout Flow

1. Proceed to Checkout Info Page
2. Fill form and continue
3. Review order → click Finish
4. Validate confirmation message

---

## ⚙️ 6. Setup & Execution

**Requirements:**

* Python ≥ 3.10
* Playwright ≥ 1.45
* pytest ≥ 7.0

```bash
# Install dependencies
pip install pytest pytest-playwright
playwright install
```

**Run all tests:**

```bash
pytest --browser=chromium -v
```

**Run headless:**

```bash
pytest --browser=chromium --headless
```

**Generate trace:**

```bash
pytest --tracing=on
```

---

## 🧱 7. Coding & Design Standards

* Follows **Page Object Model (POM)** — one class per page.
* **Encapsulation:** Each page class contains only methods for its own UI actions.
* **Separation of Concerns:** Test logic lives in `tests/`, page behavior in `pages/`.
* **Locators:** Defined as private class attributes (`_locator_name`).
* **Assertions:** Performed only in test modules, not in page classes.
* **Naming Convention:**

  * Test functions → `test_<action>_<expected>()`
  * Methods → `verb_noun()` pattern (e.g. `click_login()`).

---

## 🧰 8. Example Test

```python
# tests/test_login.py
from pages.login_page import LoginPage

def test_valid_login(page, base_url):
    login = LoginPage(page)
    login.goto(base_url)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    assert page.url.endswith("/inventory.html")
```

---

## 📊 9. Reporting & Continuous Integration

* Integrate with `pytest-html` or `allure-pytest` for detailed HTML reports.
* Use Playwright’s native **trace viewer** for debugging UI runs.
* CI Integration examples:

  * **GitHub Actions:** Run tests on push/PR with `pytest --headless`.
  * **Jenkins:** Pipeline stage for Playwright execution.

---

## 🧩 10. Maintenance Notes

* When UI elements change, update locators in Page Object files.
* Update this `.md` documentation alongside code changes.
* Regularly re-run smoke tests post UI updates.
* Keep dependencies up to date with `pip list --outdated`.

---
