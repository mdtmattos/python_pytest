import conftest
from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self):
        self.driver = conftest.driver

    #Elements
        self.page_title = (By.XPATH, '//span[@class="title"]')

    #PageObjects
    def assertLoginSuccessfully(self):
        self.driver.find_element(*self.page_title).is_displayed(), "The element '{locator}' is not visible"
