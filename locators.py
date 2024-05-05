from selenium.webdriver.common.by import By


class ProductLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(., 'Добавить в корзину')]")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    PRODUCT_NAME_MSG = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.XPATH, "//*[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRODUCT_PRICE_MSG = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")
    MSG = (By.XPATH, '//*[@id="messages"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators:
    LOGIN_LINK = ("#login_link")
    LOGIN_LINK_INVALID = ("#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = ('#login_form')
    REGISTER_FORM = ('#register_form')
