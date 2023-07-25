import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_login_invalido(self):
        loginPage = LoginPage()
        homePage = HomePage()
        
        loginPage.type_user_name("standard_user")
        loginPage.type_password("secret_sauce")
        loginPage.click_login()
        homePage.assert_login_successfully()