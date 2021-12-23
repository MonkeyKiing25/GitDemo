from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    contries = (By.XPATH, "//div[@class='suggestions']/ul/li/a")

    def findCountries(self):
        return self.driver.find_elements(*ConfirmPage.contries)