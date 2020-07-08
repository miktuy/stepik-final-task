from .base_page import BasePage
from .locators import BookOrderLocators


class BookOrderPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*BookOrderLocators.BTN_ADD_TO_BASKET), \
            "Button `Add to basket` is not found."

    def add_to_basket(self):
        self.browser.find_element(*BookOrderLocators.BTN_ADD_TO_BASKET).click()

    def should_be_at_messages(self, text):
        assert self.is_element_present(*BookOrderLocators.ADDED_MESSAGES), \
            "No messages about added products"
        messages = self.browser.find_element(*BookOrderLocators.ADDED_MESSAGES).text
        assert text in messages, f"`{text}` should be in success message"

    def get_product_title(self):
        return self.browser.find_element(*BookOrderLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*BookOrderLocators.PRODUCT_PRICE).text
