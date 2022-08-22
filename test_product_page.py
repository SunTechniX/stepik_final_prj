# pytest -v --tb=line --language=en test_product_page.py
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

#LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LINK2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.xfail(reason="presented SUCCESS after add to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = LINK
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()     # добавляем товар к корзину
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = LINK
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail(reason="not DISappeared SUCCESS after add to basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = LINK
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()                      # открываем страницу
    page.add_product_to_basket()     # добавляем товар к корзину
    page.success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = LINK2
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = LINK2
    page = ProductPage(browser, link)
    page.open()              # открываем страницу
    page.go_to_login_page()  # переходим по ссылке на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
