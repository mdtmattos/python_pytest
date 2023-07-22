import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver

    #Elements
        self.page_title = (By.XPATH, '//span[@class="title"]')

    #PageObjects
    def assertLoginSuccessfully(self):
        self.assert_element_isVisible(self.page_title)
