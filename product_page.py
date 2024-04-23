# file: product_page.py

from base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(., 'Добавить в корзину')]")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    PRODUCT_NAME_MSG = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.XPATH, "//*[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRODUCT_PRICE_MSG = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")
    MSG = (By.XPATH, '//*[@id="messages"]')

    def click_add_to_basket_btn(self):
        self.click(self.ADD_TO_BASKET_BUTTON)

    def check_product_name(self):
        product_name = self.get_text(self.PRODUCT_NAME)
        product_name_msg = self.get_text(self.PRODUCT_NAME_MSG)
        assert product_name_msg == product_name, f'Название товара в сообщении {product_name_msg} должно совпадать с тем товаром, который вы действительно добавили {product_name}.'

    def check_product_price(self):
        product_price = self.get_text(self.PRODUCT_PRICE)
        product_price_msg = self.get_text(self.PRODUCT_PRICE_MSG)
        assert product_price_msg == product_price, f'Название товара в сообщении {product_price_msg} должно совпадать с тем товаром, который вы действительно добавили {product_price}.'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.PRODUCT_NAME_MSG), \
            "Success message is presented, but should not be"

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*self.PRODUCT_NAME_MSG), \
            "Success message is presented, but should is disappeared"
