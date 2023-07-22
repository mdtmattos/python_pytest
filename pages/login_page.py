import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage): 

    def __init__(self):
        self.driver = conftest.driver

    #Elements
        self.userName_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.loginBtn = (By.ID, "login-button")
        self.loginErrorMessage = (By.XPATH, '//h3[@data-test="error"]')

    #PageObject
    def typeUserName(self, user):
        self.type(self.userName_input, user)

    def typePassword(self, password):
        self.type(self.password_input, password)

    def clickLogin(self):
        self.click(self.loginBtn)

    def assertLoginErrorMessage(self, text):
        assert self.assertText(self.loginErrorMessage), text == text