import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_login_invalido(self):
        loginPage = LoginPage()
        homePage = HomePage()
        
        loginPage.typeUserName("standard_user")
        loginPage.typePassword("secret_sauce")
        loginPage.clickLogin()
        homePage.assertLoginSuccessfully()
