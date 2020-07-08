from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "Basket is not empty"

    def should_be_empty_msg(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MSG), \
            "No message about empty basket"
