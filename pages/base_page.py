import conftest

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def type(self, locator, text):
        return self.find_element(locator).send_keys(text)
    
    def click(self, locator):
        return self.find_element(locator).click()
    
    def assert_element_isVisible(self, locator):
        return self.find_element(locator).is_displayed(), "The element '{locator}' is not visible"
    
    def assertText(self, locator):
        return self.find_element(locator).text