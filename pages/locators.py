from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TOTAL = (By.CSS_SELECTOR, "div.basket-mini")
    PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    ADDING_MESSAGE = (By.XPATH, "(//div[contains(@class, 'alertinner')]/strong)[1]")
    PRODUCT_TITLE = (By.XPATH, "//h1")
