from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_msg_about_basket_is_empty(self):
        # проверка отсутствия сообщения о пустоте корзины
        assert self.is_element_present(
            *BasketPageLocators.MSG_ABOUT_BASKET_IS_EMPTY), "Отсутствует сообщение о пустоте корзины "

    def should_not_be_items(self):
        # проверка на корректный url адрес
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Продукты присутствуют в корзине"