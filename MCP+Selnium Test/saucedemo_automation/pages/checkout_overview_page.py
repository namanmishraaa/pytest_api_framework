from playwright.sync_api import Page
from .base_page import BasePage

class CheckoutOverviewPage(BasePage):
    _URL = "/checkout-step-two.html"
    _ITEM_SUMMARY = ".cart_item"
    _FINISH_BUTTON = "#finish"

    def __init__(self, page: Page):
        super().__init__(page)

    def review_order(self):
        # This is a conceptual method. In a real scenario, you might get item details.
        return self.page.locator(self._ITEM_SUMMARY).all_text_contents()

    def click_finish(self):
        self.page.click(self._FINISH_BUTTON)
