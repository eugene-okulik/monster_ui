def test_title(sale_page):
    sale_page.open()
    assert sale_page.check_page_tittle_is('Sale')
