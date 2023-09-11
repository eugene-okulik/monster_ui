from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


send_button = (By.ID, 'send2')
email_error = (By.CSS_SELECTOR, '[role="alert"]')


class LoginPage(BasePage):
    page_url = '/customer/account/login'

    def click_send_button(self):
        self.find(send_button).click()

    def email_error_text_is(self, text):
        sleep(2)
        return self.find(email_error).text == text
