from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        with allure.step(f'Open th page {self.base_url}{self.page_url}'):
            if self.page_url:
                self.driver.get(f'{self.base_url}{self.page_url}')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)
