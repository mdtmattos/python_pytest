import conftest
from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self):
        self.driver = conftest.driver

    # Elements
    def page_title(self): 
        return self.driver.find_element(By.XPATH, '//span[@class="title"]')
    
    def product_name(self, product_name): 
        return self.driver.find_element(By.XPATH, f'//*[@class="inventory_item_name" and text()="{product_name}"]')
    
    def btn_add_to_cart(self): 
        return self.driver.find_element(By.XPATH, f'//button[@class="btn btn_primary btn_small btn_inventory" and text()="Add to cart"]')
    
    def cart_button(self):
        return self.driver.find_element(By.ID, 'shopping_cart_container')

    # Page Actions
    def assert_login_successfully(self):
        assert self.page_title().is_displayed()

    def click_product(self, product_name):
        self.product_name(product_name).click()

    def click_add_to_cart(self):
        self.btn_add_to_cart().click()
    
    def click_cart(self):
        self.cart_button().click()
