from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


page_title = (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]')


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_tittle_is(self, title):
        with allure.step(f'Check that page title is {title}'):
            title_element = self.find(page_title)
            return title_element.text == title

#  page_title - (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]')
#  *page_title - By.XPATH, '//*[@data-ui-id="page-title-wrapper"]'
