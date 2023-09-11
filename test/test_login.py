def test_error_login(login_page):
    login_page.open()
    login_page.click_send_button()
    assert login_page.email_error_text_is('A login and a password are required.')
