import time

from .base_page import BasePage
from .locators import BasketPageLocator

class BasketPage(BasePage):

    def should_not_to_be_basket(self):
        self.should_be_basket_link()
        self.go_to_basket_page()
        self.should_not_be_basket_items()
        self.should_be_basket_empty()

    def should_be_basket_link(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_LINK), "Basket link is not presented"

    def go_to_basket_page(self):
        assert self.click_is_element_present(*BasketPageLocator.BASKET_LINK), "Basket link is presented, but should not be"

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET_ITEMS), "BASKET ITEMS is presented, but should not be"

    def should_be_basket_empty(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_EMPTY), "BASKET is not empty"