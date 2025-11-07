from playwright.sync_api import Page
from .base_page import BasePage

class CartPage(BasePage):
    _URL = "/cart.html"
    _CART_ITEMS = ".cart_item"
    _CHECKOUT_BUTTON = "#checkout"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_cart_items(self) -> list[str]:
        return self.page.locator(self._CART_ITEMS).all_text_contents()

    def click_checkout(self):
        self.page.click(self._CHECKOUT_BUTTON)
