from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_button(self):
        self.should_be_button_add_to_basket()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Button is not presented"

    def should_be_alert(self):
        assert self.solve_quiz_and_get_code(), "Code not right"