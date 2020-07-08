from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.XPATH, "//a[@class='btn btn-default']")


class MainPageLocators:
    ...


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_MSG = (By.XPATH, "//div/p")


class BookOrderLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    ADDED_BOOK = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_TITLE = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
