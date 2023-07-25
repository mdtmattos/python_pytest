import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_login_invalido(self):
        loginPage = LoginPage()
        
        loginPage.type_user_name("standard_user")
        loginPage.type_password("zzzzz")
        loginPage.click_login()
        loginPage.assert_login_error_message("Epic sadface: Username and password do not match any user in this service")
