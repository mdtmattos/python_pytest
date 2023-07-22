import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_login_invalido(self):
        loginPage = LoginPage()
        
        loginPage.typeUserName("standard_user")
        loginPage.typePassword("zzzzz")
        loginPage.clickLogin()
        loginPage.assertLoginErrorMessage("Epic sadface: Username and password do not match any user in this service")
