# file: product_page.py

from base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(., 'Добавить в корзину')]")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    PRODUCT_NAME_MSG = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.XPATH, "//div/p[@='price_color']")
    PRODUCT_PRICE_MSG= (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")

    def click_add_to_basket_btn(self):
        self.click(self.ADD_TO_BASKET_BUTTON)

    def check_product_name(self):
        PRODUCT_NAME = self.get_text(self.PRODUCT_NAME)
        PRODUCT_NAME_MSG = self.get_text(self.PRODUCT_NAME_MSG)
        assert PRODUCT_NAME_MSG == PRODUCT_NAME, f'Название товара в сообщении {PRODUCT_NAME_MSG} должно совпадать с тем товаром, который вы действительно добавили {PRODUCT_NAME}.'

    def check_product_price(self):
        PRODUCT_PRICE = self.get_text(self.PRODUCT_PRICE)
        PRODUCT_PRICE_MSG = self.get_text(self.PRODUCT_PRICE_MSG)
        assert PRODUCT_PRICE_MSG == PRODUCT_PRICE, f'Название товара в сообщении {PRODUCT_PRICE_MSG} должно совпадать с тем товаром, который вы действительно добавили {PRODUCT_PRICE}.'
