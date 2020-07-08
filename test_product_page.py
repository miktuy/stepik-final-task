import pytest
from time import sleep
from pages.product_page import BookOrderPage


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    title = page.get_product_title()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_at_messages(title)


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_at_messages()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    page.should_not_be_at_messages()


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = BookOrderPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_messages()



