import time

from pages.base_page import BasePage
from locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        current_url = self.driver.current_url
        assert '/accounts/login/' in current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present(LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        print('test')