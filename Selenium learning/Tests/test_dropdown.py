from Pages.dropdown_page import DropdownPage

def test_simple_dropdown(browser):
    dropdown_pg = DropdownPage(browser)
    dropdown_pg.dropdown_open()
    assert dropdown_pg.simple_dropdown_orig_value_is_displayed == True
    dropdown_pg.simple_dropdown_value_choose('Seychelles')
    assert dropdown_pg.chosen_value_text == "Seychelles"

def test_multiple_dropdown_first_level(browser):
    dropdown_pg = DropdownPage(browser)
    dropdown_pg.dropdown_open()
    dropdown_pg.multi_dropdown()
    assert dropdown_pg.multi_dropdown_menu_is_displayed() == True
    dropdown_pg.multi_dropdown_some_action()

def test_multiple_dropdown_second_level(browser):
    dropdown_pg = DropdownPage(browser)
    dropdown_pg.dropdown_open()
    dropdown_pg.multi_dropdown()
    assert dropdown_pg.multi_dropdown_menu_is_displayed() == True
    dropdown_pg.multi_dropdown_hover_1(browser)
    assert dropdown_pg.multi_dropdown_menu_1_is_displayed() == True
    dropdown_pg.multi_dropdown_second_level()

def test_multiple_dropdown_third_level(browser):
    dropdown_pg = DropdownPage(browser)
    dropdown_pg.dropdown_open()
    dropdown_pg.multi_dropdown()
    assert dropdown_pg.multi_dropdown_menu_is_displayed() == True
    dropdown_pg.multi_dropdown_hover_1(browser)
    assert dropdown_pg.multi_dropdown_menu_1_is_displayed() == True
    dropdown_pg.multi_dropdown_hover_2(browser)
    assert dropdown_pg.multi_dropdown_menu_2_is_displayed() == True
    dropdown_pg.multi_dropdown_third_level()

def test_multiple_dropdown_fourth_level(browser):
    dropdown_pg = DropdownPage(browser)
    dropdown_pg.dropdown_open()
    dropdown_pg.multi_dropdown()
    assert dropdown_pg.multi_dropdown_menu_is_displayed() == True
    dropdown_pg.multi_dropdown_hover_1(browser)
    assert dropdown_pg.multi_dropdown_menu_1_is_displayed() == True
    dropdown_pg.multi_dropdown_hover_2(browser)
    assert dropdown_pg.multi_dropdown_menu_2_is_displayed() == True
    dropdown_pg.multi_dropdown_hover_3(browser)
    assert dropdown_pg.multi_dropdown_menu_3_is_displayed() == True
    dropdown_pg.multi_dropdown_fourth_level()