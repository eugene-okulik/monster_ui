import pytest
from selenium import webdriver
from time import sleep
from pages.sale_page import SalePage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import random


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    # sleep(3)
    yield chrome_driver
    # chrome_driver.save_screenshot(f'{random.randint(1, 5000)}.png')


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)
