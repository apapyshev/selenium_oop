from .base_page import BasePage
from .locators import ProductPageLocators

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
        assert start != end, "Product not in basket"

    def should_be_write_price(self):
        start = self.text_element_find(*ProductPageLocators.PRICE_PRODUCT)
        end = self.text_element_find(*ProductPageLocators.END_PRICE_PRODUCT)
        assert start != end, f"Price not correct {start} -> {end}"

    def should_be_alert(self):
        self.click_element(*ProductPageLocators.ADD_BASKET)
        code = self.solve_quiz_and_get_code()
        assert code is True, "No second alert presented"