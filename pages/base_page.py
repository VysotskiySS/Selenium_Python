import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        # открыть страницу
        return self.driver.get(self.url)

    def go_to_basket_page(self):
        # перейти в корзину
        link = self.driver.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def find_element(self, locator, time=10):
        # поиск элемента
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удалось найти элемент по локатору: {str(locator)}")

    def find_elements(self, locator, time=10):
        # поиск элементов
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не удалось найти элементы по локатору: {str(locator)}")

    def get_element(self, locator):
        # получить элемент
        element = self.find_element(locator)
        return element

    def click(self, locator):
        # клик по элементу
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, value):
        # ввести текст
        textarea = self.find_element(locator)
        textarea.send_keys(value)

    def get_text(self, locator):
        # получить текст элемента
        text = self.find_element(locator).text
        return text

    def solve_quiz_and_get_code(self):
        # решение капчи
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        # проверка, что элемента нет на странице
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        # проверка, что элемент исчезает
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        # проверка, что элемент отображается
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        # переход к странице регистрации и авторизации
        login_link = self.driver.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        # проверка, что ссылка на страницу регистрации и авторизации есть
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        # проверка, что пользователь авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented"
