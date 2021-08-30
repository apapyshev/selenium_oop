from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


@pytest.mark.xfail(reason="Success message is presented, but should not be")
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_button_add_to_basket()
    product_page.should_be_click()
    product_page.should_not_be_success_message()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()

@pytest.mark.skip()
@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_button_add_to_basket()
    product_page.should_be_click()
    product_page.should_not_be_disappeared_message()