# pytest -v --tb=line --language=en test_main_page.py
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    login_page = page.go_to_login_page()  # переходим по ссылкы на страницу логина
    login_page.should_be_login_page()
