# file: product_page.py

from pages.base_page import BasePage
from pages.locators import ProductLocators


class ProductPage(BasePage):


    def click_add_to_basket_btn(self):
        self.click(ProductLocators.ADD_TO_BASKET_BUTTON)

    def check_product_name(self):
        product_name = self.get_text(ProductLocators.PRODUCT_NAME)
        product_name_msg = self.get_text(ProductLocators.PRODUCT_NAME_MSG)
        assert product_name_msg == product_name, f'Название товара в сообщении {product_name_msg} должно совпадать с тем товаром, который вы действительно добавили {product_name}.'

    def check_product_price(self):
        product_price = self.get_text(ProductLocators.PRODUCT_PRICE)
        product_price_msg = self.get_text(ProductLocators.PRODUCT_PRICE_MSG)
        assert product_price_msg == product_price, f'Название товара в сообщении {product_price_msg} должно совпадать с тем товаром, который вы действительно добавили {product_price}.'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.SUCCESS_MESSAGE) == True, \
            "Success message is presented, but should not be"

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductLocators.SUCCESS_MESSAGE) == True, \
            "Success message is presented, but should is disappeared"
