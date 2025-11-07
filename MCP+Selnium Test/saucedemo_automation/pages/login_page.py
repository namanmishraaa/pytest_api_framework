from playwright.sync_api import Page
from .base_page import BasePage

class LoginPage(BasePage):
    _URL = "/"
    _USERNAME_INPUT = "#user-name"
    _PASSWORD_INPUT = "#password"
    _LOGIN_BUTTON = "#login-button"
    _ERROR_MESSAGE = ".error-message-container"

    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self, base_url: str):
        super().goto(f"{base_url}{self._URL}")

    def enter_username(self, username: str):
        self.page.fill(self._USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.page.fill(self._PASSWORD_INPUT, password)

    def click_login(self):
        self.page.click(self._LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.page.text_content(self._ERROR_MESSAGE)
