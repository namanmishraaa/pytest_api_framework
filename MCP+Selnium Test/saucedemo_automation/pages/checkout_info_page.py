from playwright.sync_api import Page
from .base_page import BasePage

class CheckoutInfoPage(BasePage):
    _URL = "/checkout-step-one.html"
    _FIRST_NAME_INPUT = "#first-name"
    _LAST_NAME_INPUT = "#last-name"
    _POSTAL_CODE_INPUT = "#postal-code"
    _CONTINUE_BUTTON = "#continue"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_shipping_info(self, first: str, last: str, zip_code: str):
        self.page.fill(self._FIRST_NAME_INPUT, first)
        self.page.fill(self._LAST_NAME_INPUT, last)
        self.page.fill(self._POSTAL_CODE_INPUT, zip_code)

    def click_continue(self):
        self.page.click(self._CONTINUE_BUTTON)
