from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    PRODUCT_NAME_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRODUCT_PRICE_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(3) .alertinner strong")
    MSG = (By.XPATH, '//*[@id="messages"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    MSG_ABOUT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, 'div#content_inner p')