import allure
import pytest


@pytest.mark.failed
@allure.feature('Login')
@allure.story('Negative')
def test_error_login(login_page):
    with allure.step('Open login page'):
        login_page.open()
    with allure.step('Click send button'):
        login_page.click_send_button()
    with allure.step('Check that error text is correct'):
        assert login_page.email_error_text_is('A login and a password are required.')


@pytest.mark.smoke
@allure.feature('Login')
@allure.story('Positive')
def test_1_is_1():
    assert 1 == 1
