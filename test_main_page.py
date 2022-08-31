# pytest -v -m "login_guest" --tb=line --language=en test_main_page.py
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        link = LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


    @pytest.mark.empty
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()  # переходим по ссылке в корзину
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_basket_summary()
        basket_page.should_be_empty_basket_msg()
