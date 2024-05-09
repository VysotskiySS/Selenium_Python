# file: test_product_page.py
import pytest
import random
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage


class TestProductPage:
    link_product_with_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    link_product = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link_product_with_promo)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.check_product_name()
        page.check_product_price()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link_product)
        page.open()
        page.click_add_to_basket_btn()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link_product)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link_product)
        page.open()
        page.click_add_to_basket_btn()
        page.is_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items()
        basket_page.should_be_msg_about_basket_is_empty()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    login_link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    link_product_with_promo = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, self.login_link)
        base_page = BasePage(browser, browser.current_url)
        login_page.open()
        email = str(random.randint(0, 99999999)) + "@mail.org"
        login_page.register_new_user(email, 'Password123!')
        base_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.product_link)
        browser.get(self.product_link)
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link_product_with_promo)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.check_product_name()
        page.check_product_price()
