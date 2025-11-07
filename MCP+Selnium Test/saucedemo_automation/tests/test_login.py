from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_valid_login(page: Page, base_url: str):
    login = LoginPage(page)
    login.goto(base_url)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    assert page.url.endswith("/inventory.html")


def test_invalid_login(page: Page, base_url: str):
    login = LoginPage(page)
    login.goto(base_url)
    login.enter_username("locked_out_user")
    login.enter_password("secret_sauce")
    login.click_login()
    assert "Epic sadface: Sorry, this user has been locked out." in login.get_error_message()
