from Pages.pagination_page import PaginationPage

def test_page_1_btn(browser):
    pagination_pg = PaginationPage(browser)
    pagination_pg.pagination_open()
    pagination_pg.page_1_button()
    assert pagination_pg.page_1_alert_is_displayed() == True
    assert pagination_pg.page_1_alert_text() == 'You clicked page no. 1'

def test_page_2_btn(browser):
    pagination_pg = PaginationPage(browser)
    pagination_pg.pagination_open()
    pagination_pg.page_2_button()
    assert pagination_pg.page_2_alert_is_displayed() == True
    assert pagination_pg.page_2_alert_text() == 'You clicked page no. 2'

def test_page_3_btn(browser):
    pagination_pg = PaginationPage(browser)
    pagination_pg.pagination_open()
    pagination_pg.page_3_button()
    assert pagination_pg.page_3_alert_is_displayed() == True
    assert pagination_pg.page_3_alert_text() == 'You clicked page no. 3'

def test_next_page_btn(browser):
    pagination_pg = PaginationPage(browser)
    pagination_pg.pagination_open()
    pagination_pg.next_page_button()
    assert pagination_pg.next_page_alert_is_displayed() == True
    assert pagination_pg.next_page_alert_text() == 'You clicked the "Next" button'