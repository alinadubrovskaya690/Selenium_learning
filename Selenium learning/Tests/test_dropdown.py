from Pages.dropdown_page import DropdownPage
import time

def test_simple_dropdown(browser):
    dropdown_pg = DropdownPage(browser)
    dropdown_pg.dropdown_open()
    assert dropdown_pg.simple_dropdown_orig_value_is_displayed == True
    dropdown_pg.simple_dropdown_value_choose('Seychelles')
    assert dropdown_pg.chosen_value_text == True
    time.sleep(5)