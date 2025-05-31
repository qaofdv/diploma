from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def total_is_equal_with_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_text = self.browser.find_element(*ProductPageLocators.TOTAL).text
        assert price in basket_text

    def adding_message_is_equal_with_product_title(self):
        adding_message = self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE)
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        assert product_title.text == adding_message.text
