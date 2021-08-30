from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest


product_link_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="
links = [f"{product_link_base}{number}" for number in ('offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6', 'offer7', 'offer8', 'offer9')]

@pytest.mark.skip()
@pytest.mark.xfail(number="offer7")
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    print(link)
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_add_button()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()