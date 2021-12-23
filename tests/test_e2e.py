#Import cac package can thiet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        driver = self.driver
        homePage = HomePage(driver)
        checkoutPage = homePage.shopItems()
        confirmPage = ConfirmPage(driver)
        products = checkoutPage.getProducts()

        log.info("getting all the card titles")
        # Chon san pham Blackberry
        for product in products:
            productName = product.find_element(*checkoutPage.cartTitle).text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                self.elementAction("//li/a[@class='nav-link btn btn-primary']")
                self.waitElement("//td/button[@class='btn btn-success']")
                self.elementAction("//td/button[@class='btn btn-success']")
                self.waitElement("//div/input[@type='text']")
                driver.find_element(
                    By.XPATH, "//div/input[@type='text']").send_keys("in")
                self.waitElement("//div[@class='suggestions']/ul/li/a")
                log.info("Entering country name as ind")

                countries = confirmPage.findCountries()
                # Chon quoc gia de van chuyen hang
                for country in countries:
                    if country.text == "India":
                        driver.execute_script("arguments[0].click();", country)
                        break
                self.elementAction("//div[@class='checkbox checkbox-primary']")
                self.elementAction("//input[@class='btn btn-success btn-lg']")
                self.waitElement(
                    "//div[@class='alert alert-success alert-dismissible']")
                text = driver.find_element(
                    By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
                log.info("Text received from application is "+ text)
                assert "Success!" in text
                time.sleep(2)
