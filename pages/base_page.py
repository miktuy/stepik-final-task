from selenium import webdriver


class BasePage:
    def __init__(self, browser: webdriver.Chrome, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)