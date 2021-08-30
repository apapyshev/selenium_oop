from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def should_be_add_button(self):
        self.should_be_button_add_to_basket()
        self.should_be_alert()
        self.should_be_in_basket_product()
        self.should_be_write_price()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Button is not presented"

    def should_be_in_basket_product(self):
        start = self.text_element_find(*ProductPageLocators.TEXT_PRODUCT)
        end = self.text_element_find(*ProductPageLocators.END_TEXT_PRODUCT)
        assert start.text != end.text, "Product not in basket"

    def should_be_write_price(self):
        start = self.text_element_find(*ProductPageLocators.PRICE_PRODUCT)
        end = self.text_element_find(*ProductPageLocators.END_PRICE_PRODUCT)
        assert start.text != end.text, f"Price not correct {start} -> {end}"

    def should_be_alert(self):
        self.click_element(*ProductPageLocators.ADD_BASKET)
        code = self.solve_quiz_and_get_code()
        assert code == True, "No second alert presented"

    def should_be_click(self):
        self.click_element(*ProductPageLocators.ADD_BASKET)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared_message(self):
        self.click_element(*ProductPageLocators.ADD_BASKET)
        time.sleep(1)
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"