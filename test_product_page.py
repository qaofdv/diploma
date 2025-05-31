from .pages.product_page import ProductPageLocators, ProductPage
from .pages.base_page import BasePage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    product_page.total_is_equal_with_price()
    product_page.adding_message_is_equal_with_product_title()




