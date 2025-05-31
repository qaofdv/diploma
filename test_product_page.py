from .pages.product_page import ProductPageLocators, ProductPage
from .pages.base_page import BasePage
import pytest

@pytest.mark.parametrize('offer', [
    "offer0",
    "offer1",
    "offer2",
    "offer3",
    "offer4",
    "offer5",
    "offer6",
    pytest.param("offer7", marks=pytest.mark.xfail),
    "offer8",
    "offer9"
])

def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    product_page.total_is_equal_with_price()
    product_page.adding_message_is_equal_with_product_title()




