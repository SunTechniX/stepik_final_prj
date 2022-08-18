from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    HAS_BEEN_ADDED = (By.CSS_SELECTOR, "div.alert-success > div.alertinner")
    BASKET_NAME = (By.CSS_SELECTOR, "div.alert-success > div.alertinner > strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info > div.alertinner > p > strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
