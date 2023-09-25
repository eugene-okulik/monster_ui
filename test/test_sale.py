import allure
import pytest


@pytest.mark.regression
@allure.feature('Sale')
@allure.story('Tile')
def test_title(sale_page):
    sale_page.open()
    assert sale_page.check_page_tittle_is('Sale')


@pytest.mark.smoke
@allure.feature('Sale')
@allure.story('Products')
def test_total():
    assert 1 == 1
