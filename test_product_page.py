# file: test_product_page.py
from product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser)
    page.click_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.check_product_name()
    page.check_product_price()
