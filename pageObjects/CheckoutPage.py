from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    
    product = (By.XPATH, "//div[@class='card h-100']")

    cartTitle = (By.XPATH, "div/h4/a")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.product)


