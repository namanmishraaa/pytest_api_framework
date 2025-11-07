from playwright.sync_api import Page
from .base_page import BasePage

class CheckoutCompletePage(BasePage):
    _URL = "/checkout-complete.html"
    _CONFIRMATION_MESSAGE = ".complete-header"
    _BACK_HOME_BUTTON = "#back-to-products"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_confirmation_message(self) -> str:
        return self.page.text_content(self._CONFIRMATION_MESSAGE)

    def click_back_home(self):
        self.page.click(self._BACK_HOME_BUTTON)
