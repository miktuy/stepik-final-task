import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: ...")
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\n Start Chrome browser for test...")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        options.add_argument("--incognito")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\n Start Firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(3)
    yield browser
    browser.quit()
