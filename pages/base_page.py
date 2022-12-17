import pytest
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from .locators import BasePageLocators
from .locators import ProductPageLocators
import math
import time

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        print('==>> open self.url')
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(2)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def solve_quiz_and_get_code_ff(self):
        try:
            WebDriverWait(self.browser, 3).until(EC.alert_is_present())  # ожидание alert - в FireFox тормозится
        except TimeoutException:
            print("Timeout 3 sec for Alert 1 window")
        except NoSuchElementException:
            print("No Such Element: Alert 1 window")
        except NoAlertPresentException:
            print("No Alert 1 presented first time")

        # time.sleep(3)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(2)
        try:
            WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_logout(self):
        link = self.browser.find_element(*BasePageLocators.LOGOUT_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_VIEW)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
            " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_logout_link(self):
        assert self.is_element_present(*BasePageLocators.LOGOUT_LINK), "Logout link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True

    def is_element_present_v2(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:  # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        print('WAIT 4 seconds [disappear]')
        try: # будет ждать до тех пор, пока элемент не исчезнет
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
