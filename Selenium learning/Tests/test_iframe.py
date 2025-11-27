from Pages.iframe_page import IframePage

def test_navbar_btn(browser):
    iframe_pg = IframePage(browser)
    iframe_pg.iframe_open()
    iframe_pg.iframe_switch()
    iframe_pg.navbar_button()