from Pages.iframe_page import IframePage

def test_navbar_btn(browser):
    iframe_pg = IframePage(browser)
    iframe_pg.iframe_open()
    iframe_pg.iframe_switch()
    iframe_pg.navbar_button()

def test_home_btn(browser):
    iframe_pg = IframePage(browser)
    iframe_pg.iframe_open()
    iframe_pg.iframe_switch()
    iframe_pg.home_button()

def test_features_btn(browser):
    iframe_pg = IframePage(browser)
    iframe_pg.iframe_open()
    iframe_pg.iframe_switch()
    iframe_pg.features_button()

def test_pricing_btn(browser):
    iframe_pg = IframePage(browser)
    iframe_pg.iframe_open()
    iframe_pg.iframe_switch()
    iframe_pg.pricing_button()

def test_learn_more_btn(browser):
    iframe_pg = IframePage(browser)
    iframe_pg.iframe_open()
    iframe_pg.iframe_switch()
    iframe_pg.learn_more_button()
    assert iframe_pg.learn_more_text_is_displayed() == True
    assert iframe_pg.learn_more_text() == 'This text appears when you click the "Learn more" button'