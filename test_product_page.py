from time import sleep
from pages.product_page import BookOrderPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = BookOrderPage(browser, link)
    page.open()
    title = page.get_product_title()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # sleep(600)
    page.should_be_at_messages(title)
    # sleep(600)