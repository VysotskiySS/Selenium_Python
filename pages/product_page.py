# file: product_page.py

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_btn(self):
        self.click(ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def check_product_name(self):
        product_name = self.get_text(ProductPageLocators.PRODUCT_NAME)
        product_name_msg = self.get_text(ProductPageLocators.PRODUCT_NAME_MSG)
        assert product_name_msg == product_name, f'Название товара в сообщении {product_name_msg} должно совпадать с тем товаром, который вы действительно добавили {product_name}.'

    def check_product_price(self):
        product_price = self.get_text(ProductPageLocators.PRODUCT_PRICE)
        product_price_msg = self.get_text(ProductPageLocators.PRODUCT_PRICE_MSG)
        assert product_price_msg == product_price, f'Название товара в сообщении {product_price_msg} должно совпадать с тем товаром, который вы действительно добавили {product_price}.'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is presented, but should not be"

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is presented, but should is disappeared"
