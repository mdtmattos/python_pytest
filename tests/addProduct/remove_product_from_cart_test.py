import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_add_product_to_cart(self):
        loginPage = LoginPage()
        homePage = HomePage()
        cartPage = CartPage()
        
        # Login
        loginPage.type_user_name('standard_user')
        loginPage.type_password('secret_sauce')
        loginPage.click_login()
        homePage.assert_login_successfully()

        # Add Product To Cart
        homePage.click_product('Sauce Labs Backpack')
        homePage.click_add_to_cart()
        homePage.click_cart()
        cartPage.assert_page_title('Your Cart')
        cartPage.assert_product_name('Sauce Labs Backpack')

        # Remove Product
        cartPage.click_remove_btn()
        cartPage.assert_product_not_visible('Sauce Labs Backpack')