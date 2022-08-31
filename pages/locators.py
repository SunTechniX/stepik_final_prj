from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_VIEW = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form.basket_summary")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner > p")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR,"input#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REGISTER_SUCCESS_MSG = (By.CSS_SELECTOR,"div.alert-success")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success > div.alertinner")
    BASKET_NAME = (By.CSS_SELECTOR, "div.alert-success > div.alertinner > strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info > div.alertinner > p > strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

