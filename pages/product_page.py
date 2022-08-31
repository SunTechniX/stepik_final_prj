import pytest
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_on_basket_button()
        #self.solve_quiz_and_get_code()   # Запустить решение и получение кода
        self.solve_quiz_and_get_code_ff()   # Запустить решение и получение кода
        print('sleep 2 sec after solve code')
        time.sleep(2)
        self.check_product_name_in_basket()
        self.check_product_price_in_basket()

    def click_on_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def check_product_in_basket(self):
        WebDriverWait(self.browser, 5).until(EC.is_element_present(*ProductPageLocators.BASKET_NAME))
        assert WebDriverWait(self.browser, 5).until(
            EC.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        ), "Product not added to Basket!"

    def check_product_name_in_basket(self):
        name_prod = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_basket = self.browser.find_element(*ProductPageLocators.BASKET_NAME)
        assert name_prod.text == name_basket.text, "Product name not equal name in Basket!"

    def check_product_price_in_basket(self):
        price_prod = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price_prod.text == price_basket.text, "Product price not equal price in Basket!"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be - should is disappeared!"
