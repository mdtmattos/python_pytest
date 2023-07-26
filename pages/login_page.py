import conftest
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self):
        self.driver = conftest.driver

    # Elements
    def user_name_input(self): 
        return self.driver.find_element(By.ID, "user-name")
    
    def password_input(self):
        return self.driver.find_element(By.ID, "password")
        
    def login_btn(self):
        return self.driver.find_element(By.ID, "login-button")
    
    def login_error_messages(self):
        return self.driver.find_elements(By.XPATH, '//h3[@data-test="error"]')

    # Page Actions
    def assert_login_error_message(self, text):
        error_messages = [element.text for element in self.login_error_messages()]
        assert text in error_messages

    def assert_user_name_field_is_visible(self):
        self.user_name_input().is_displayed()

    def click_login(self):
        self.login_btn().click()

    def type_user_name(self, user):
        self.user_name_input().send_keys(user)

    def type_password(self, password):
        self.password_input().send_keys(password)