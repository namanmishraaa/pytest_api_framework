from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_to_cart(page: Page, base_url: str):
    # Login first
    login_page = LoginPage(page)
    login_page.goto(base_url)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    assert page.url.endswith("/inventory.html")

    # Add item to cart
    products_page = ProductsPage(page)
    products_page.add_to_cart("Sauce Labs Backpack")
    assert products_page.get_cart_count() == 1

    # Open cart and verify
    products_page.open_cart()
    assert page.url.endswith("/cart.html")
