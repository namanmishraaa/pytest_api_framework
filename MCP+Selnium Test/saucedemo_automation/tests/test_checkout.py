from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_flow(page: Page, base_url: str):
    # 1. Login
    login_page = LoginPage(page)
    login_page.goto(base_url)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 2. Add item to cart
    products_page = ProductsPage(page)
    products_page.add_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    # 3. Proceed to Checkout
    cart_page = CartPage(page)
    cart_page.click_checkout()
    assert page.url.endswith("/checkout-step-one.html")

    # 4. Fill shipping info
    checkout_info_page = CheckoutInfoPage(page)
    checkout_info_page.fill_shipping_info("Test", "User", "12345")
    checkout_info_page.click_continue()
    assert page.url.endswith("/checkout-step-two.html")

    # 5. Finish order
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_page.click_finish()
    assert page.url.endswith("/checkout-complete.html")

    # 6. Validate confirmation message
    checkout_complete_page = CheckoutCompletePage(page)
    confirmation_message = checkout_complete_page.get_confirmation_message()
    assert confirmation_message == "Thank you for your order!"
