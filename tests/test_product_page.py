# file: test_product_page.py
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from config import *

from pages.product_page import ProductPage


def test_registration(browser):
    page = ProductPage(browser)
    page.click_add_to_basket_btn()
    time.sleep(100)
