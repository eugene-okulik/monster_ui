import pytest
from selenium import webdriver
from time import sleep
from pages.sale_page import SalePage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    sleep(3)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)
