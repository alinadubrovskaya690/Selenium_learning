from Pages.login_page import LoginPage
import time

def test_valid_login(browser):
    login_pg = LoginPage(browser)
    login_pg.login_open()
    login_pg.login_email_enter('admin@admin.com')
    login_pg.login_password_enter('admin123')
    login_pg.login_confirm()
    assert login_pg.login_main_page_is_displayed == True
    time.sleep(5)

def test_invalid_login(browser):
    login_pg = LoginPage(browser)
    login_pg.login_open()
    login_pg.login_email_enter('adminadmin.com')
    login_pg.login_password_enter('a')
    login_pg.login_confirm()
    assert login_pg.login_main_page_is_displayed == False
    assert login_pg.message_is_displayed == True
    assert login_pg.message_text == 'Bad credentials! Please try again! Make sure that you\'ve registered.'
    time.sleep(5)

def test_empty_login(browser):
    login_pg = LoginPage(browser)
    login_pg.login_open()
    login_pg.login_email_enter('')
    login_pg.login_password_enter('')
    login_pg.login_confirm()
    assert login_pg.login_main_page_is_displayed == False
    assert login_pg.message_is_displayed == True
    assert login_pg.message_text == 'Bad credentials! Please try again! Make sure that you\'ve registered.'
    time.sleep(5)