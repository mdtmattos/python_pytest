import conftest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CartPage():
    def __init__(self):
        self.driver = conftest.driver

    # Elements
    def page_title(self): 
        return self.driver.find_element(By.XPATH, '//span[@class="title"]')
    
    def product_title(self, product_name): 
        return self.driver.find_element(By.XPATH, f'//*[@class="inventory_item_name" and text()="{product_name}"]')
    
    def checkout_btn(self): 
        return self.driver.find_element(By.ID, 'checkout')
    
    def remove_btn(self):
        return self.driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    
    def continue_shipping_btn(self):
        return self.driver.find_element(By.ID, 'continue-shopping')
    
    def continue_btn(self):
        return self.driver.find_element(By.ID, 'continue')
    
    def finish_btn(self):
        return self.driver.find_element(By.ID, 'finish')
    
    def input_first_name(self): 
        return self.driver.find_element(By.ID, 'first-name')
    
    def input_last_name(self): 
        return self.driver.find_element(By.ID, 'last-name')
    
    def input_zip_code(self): 
        return self.driver.find_element(By.ID, 'postal-code')
    
    def payment_info_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="payment-info-label"]')
    
    def shipping_info_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="shipping-info-label"]')
    
    def total_info_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="total-info-label"]')
    
    def checkout_successful_message(self, message):
        return self.driver.find_element(By.XPATH, f'//h2[@class="complete-header" and text()="{message}"]')

    # Page Actions
    def assert_page_title(self, title):
        assert self.page_title().text == title

    def assert_product_name(self, product_name):
        assert self.product_title(product_name).text == product_name

    def assert_checkout_successful_message(self, message):
        assert self.checkout_successful_message(message).text == message

    def assert_product_not_visible(self, product_name):
        try:
            assert not self.product_title(product_name), f"Product '{product_name}' is visible, but it should not be."
        except NoSuchElementException:
            pass

    def assert_checkout_payment_information(self, text):
        assert self.payment_info_label().is_displayed()
        assert self.payment_info_label().text == text, f"Expected text to be '{text}', but got '{self.payment_info_label().text}'"

    def assert_checkout_shipping_information(self, text):
        assert self.shipping_info_label().is_displayed()
        assert self.shipping_info_label().text == text, f"Expected text to be '{text}', but got '{self.shipping_info_label().text}'"

    def assert_checkout_price_information(self, text):
        assert self.total_info_label().is_displayed()
        assert self.total_info_label().text == text, f"Expected text to be '{text}', but got '{self.total_info_label().text}'"

    def click_checkout_btn(self):
        self.checkout_btn().click()
    
    def click_continue_shipping(self):
        self.continue_shipping_btn().click()

    def click_remove_btn(self):
        self.remove_btn().click()

    def click_continue_btn(self):
        self.continue_btn().click()

    def click_finish_btn(self):
        self.finish_btn().click()

    def type_first_name(self, first_name):
        self.input_first_name().send_keys(first_name)
    
    def type_last_name(self, last_name):
        self.input_last_name().send_keys(last_name)

    def type_zip_code(self, zip_code):
        self.input_zip_code().send_keys(zip_code)