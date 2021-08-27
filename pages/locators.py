from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    LOGIN_URL = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    TEXT_PRODUCT = (By.XPATH, "//ul[@class='breadcrumb']/li[@class='active']")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main p.price_color")
    END_TEXT_PRODUCT = (By.XPATH, "//div[@id='messages']/div/div/strong")
    END_PRICE_PRODUCT = (By.CSS_SELECTOR, "div.alertinner p strong")
