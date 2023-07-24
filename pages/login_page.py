import conftest
from selenium.webdriver.common.by import By


class LoginPage(): 

    def __init__(self):
        self.driver = conftest.driver

    #Elements
        self.userName_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.loginBtn = (By.ID, "login-button")
        self.loginErrorMessage = (By.XPATH, '//h3[@data-test="error"]')

    #PageObject
    def typeUserName(self, user):
        self.driver.find_element(*self.userName_input).send_keys(user)

    def typePassword(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.loginBtn).click()

    def assertLoginErrorMessage(self, text):
        assert self.driver.find_element(*self.loginErrorMessage), text == text