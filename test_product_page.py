# pytest -v --tb=line --language=en test_product_page.py
import pytest
from .pages.product_page import ProductPage

#LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

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
