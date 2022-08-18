import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_Chrome
#from selenium.webdriver.chrome.options import Options as Options_FireFox
import os

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, es, ... etc")  # +++
    parser.addoption('--headless', action='store', default='true',
                     help="Open a browser invisible, without GUI is used by default")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")  # +++
    headless = request.config.getoption('headless')
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = Options_Chrome()        # chrome_options.add_argument('headless')
        # chrome_options.add_argument('window-size=1920x935')
        if headless == 'true':
            chrome_options.add_argument('headless')
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        # Без браузерный режим для 'Firefox', через импорт библиотеки 'os'
        if headless == 'true':
            os.environ['MOZ_HEADLESS'] = '1'
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser..")
    browser.quit()
