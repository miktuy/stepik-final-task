from .base_page import BasePage
from .locators import BookOrderLocators


class BookOrderPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*BookOrderLocators.BTN_ADD_TO_BASKET), \
            "Button `Add to basket` is not found."

    def add_to_basket(self):
        self.browser.find_element(*BookOrderLocators.BTN_ADD_TO_BASKET).click()

    def should_be_at_messages(self, text):
        assert self.is_element_present(*BookOrderLocators.ADDED_BOOK), \
            "No messages about added products"
        msg = self.browser.find_element(*BookOrderLocators.ADDED_BOOK).text
        assert text == msg, f"`{text}` should be in success message. Now is `{msg}`"

    def should_not_be_at_messages(self):
        assert self.is_not_element_present(*BookOrderLocators.ADDED_BOOK), \
            "Should not be success message"

    def should_be_disappeared_messages(self):
        assert self.is_disappeared(*BookOrderLocators.ADDED_BOOK), \
            "message should disappear during time"

    def get_product_title(self):
        return self.browser.find_element(*BookOrderLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*BookOrderLocators.PRODUCT_PRICE).text
