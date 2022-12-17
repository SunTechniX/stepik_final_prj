# pytest -v -m login_user --tb=line --language=en test_product_page.py
import pytest
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

#LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LINK2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    link = LINK

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.delete_all_cookies()
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()  # переходим по ссылке на страницу логина/регистрации
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@xmail.org"
        password = 'x' + str(time.time()) + 'z'
        login_page.register_new_user(email, password)  # зарегистрировать нового пользователя;
        login_page.should_be_authorized_user()  # проверить, что пользователь залогинен.

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_basket()     # добавляем товар к корзину

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()     # добавляем товар в корзину

def test_guest_cant_see_success_message(browser):
    link = LINK
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="presented SUCCESS after add to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = LINK
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()     # добавляем товар в корзину
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="not DISappeared SUCCESS after add to basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = LINK
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()     # добавляем товар к корзину
    page.success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = LINK2
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = LINK2
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # переходим по ссылке на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
@pytest.mark.empty
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = LINK2
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()  # переходим по ссылке в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_summary()
    basket_page.should_be_empty_basket_msg()
