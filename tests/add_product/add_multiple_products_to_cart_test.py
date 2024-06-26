import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_add_multiple_product_to_cart(self):
        loginPage = LoginPage()
        homePage = HomePage()
        cartPage = CartPage()
        
        # Login
        loginPage.type_user_name('standard_user')
        loginPage.type_password('secret_sauce')
        loginPage.click_login()
        homePage.assert_login_successfully()

        # Add Multiple Products To Cart
        homePage.click_product('Sauce Labs Backpack')
        homePage.click_add_to_cart()
        homePage.click_cart()
        cartPage.assert_page_title('Your Cart')
        cartPage.assert_product_name('Sauce Labs Backpack')
        cartPage.click_continue_shipping()
        homePage.click_product('Sauce Labs Bike Light')
        homePage.click_add_to_cart()
        homePage.click_cart()
        cartPage.assert_page_title('Your Cart')
        cartPage.assert_product_name('Sauce Labs Bike Light')
        cartPage.click_continue_shipping()
        homePage.click_product('Sauce Labs Fleece Jacket')
        homePage.click_add_to_cart()
        homePage.click_cart()
        cartPage.assert_page_title('Your Cart')
        cartPage.assert_product_name('Sauce Labs Fleece Jacket')

        # Checkout Product
        cartPage.click_checkout_btn()
        cartPage.type_first_name('Pytest')
        cartPage.type_last_name('Automation')
        cartPage.type_zip_code('80122000')
        cartPage.click_continue_btn()

        # Assert Details
        cartPage.assert_page_title('Checkout: Overview')
        cartPage.assert_product_name('Sauce Labs Backpack')
        cartPage.assert_product_name('Sauce Labs Bike Light')
        cartPage.assert_product_name('Sauce Labs Fleece Jacket')
        cartPage.assert_checkout_payment_information('Payment Information:')
        cartPage.assert_checkout_shipping_information('Shipping Information:')
        cartPage.assert_checkout_price_information('Price Total')
        
        # Finishing checkout
        cartPage.click_finish_btn()
        cartPage.checkout_successful_message('Thank you for your order!')