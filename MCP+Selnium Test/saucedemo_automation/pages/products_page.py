from playwright.sync_api import Page
from .base_page import BasePage

class ProductsPage(BasePage):
    _URL = "/inventory.html"
    _ITEM_TITLE = ".inventory_item_name"
    _ADD_TO_CART_BUTTON = ".btn_inventory"
    _CART_ICON = ".shopping_cart_link"
    _CART_BADGE = ".shopping_cart_badge"

    def __init__(self, page: Page):
        super().__init__(page)

    def add_to_cart(self, item_name: str):
        item_container = self.page.locator(".inventory_item", has_text=item_name)
        item_container.locator(self._ADD_TO_CART_BUTTON).click()

    def open_cart(self):
        self.page.click(self._CART_ICON)

    def get_cart_count(self) -> int:
        badge_text = self.page.text_content(self._CART_BADGE)
        return int(badge_text) if badge_text else 0
