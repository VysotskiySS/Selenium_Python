# file: product_page.py

from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(., 'Добавить в корзину')]")

    def click_add_to_basket_btn(self):
        self.click(self.ADD_TO_BASKET_BUTTON)
