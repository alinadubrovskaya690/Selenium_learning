from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random


URL = 'https://qa-practice.netlify.app/dropdowns'

simple_dropdown = (By.XPATH, '//*[@id = "dropdown-menu"]')
simple_dropdown_orig_value = (By.XPATH, '//option[text() = "Select a country..."]')
simple_dropdown_value = (By.XPATH, '//option[text() = "Seychelles"]')

multiple_dropdown = (By.XPATH, '//*[@id = "multi-level-dropdown-btn"]')
multiple_dropdown_value = (By.XPATH, '//a[text() = "Some action"]')
multiple_dropdown_menu = (By.XPATH, '//*[@id = "multi-level-menu-ul"]')
multiple_dropdown_hover_1 = (By.XPATH, '//a[text() = "Hover me for more options"]')
multiple_dropdown_menu_1 = (By.XPATH, '//li[@class="dropdown-submenu"]')
multiple_dropdown_value_1 = (By.XPATH, '//a[text() = "Second level - 1"]')
multiple_dropdown_hover_2 = (By.XPATH, '//a[text() = "Even More.."]')
multiple_dropdown_menu_2 = (By.XPATH, '//li[@class="dropdown-submenu"]')
multiple_dropdown_value_2 = (By.XPATH, '//a[text() = "3rd level - 2"]')
multiple_dropdown_hover_3 = (By.XPATH, '//a[text() = "another level"]')
multiple_dropdown_menu_3 = (By.XPATH, '//li[@class="dropdown-submenu"]')
multiple_dropdown_value_3 = (By.XPATH, '//a[text() = "4th level - 3"]')


class DropdownPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def dropdown_open(self):
        self.open(URL)

    def simple_dropdown_value_choose(self, value):
        country_value = Select(self.find(simple_dropdown))
        country_value.select_by_value(value)

    def simple_dropdown_value_random_choose(self, value):
        country_value = Select(self.find(simple_dropdown))
        country_value.select_by_visible_text(random.choice(value))

    @property
    def simple_dropdown_orig_value_is_displayed(self):
        return self.find(simple_dropdown_orig_value).is_displayed()

    @property
    def chosen_value_text(self):
        return self.find(simple_dropdown_value).text

    def multi_dropdown(self):
        return self.find(multiple_dropdown).click()

    def multi_dropdown_some_action(self):
        return self.find(multiple_dropdown_value).click()

    def multi_dropdown_menu_is_displayed(self):
        return self.find(multiple_dropdown_menu).is_displayed()

    def multi_dropdown_hover_1(self, browser):
        action = ActionChains(browser)
        action.move_to_element(self.find(multiple_dropdown_hover_1)).perform()

    def multi_dropdown_menu_1_is_displayed(self):
        return self.find(multiple_dropdown_menu_1).is_displayed()

    def multi_dropdown_second_level(self):
        return self.find(multiple_dropdown_value_1).click()

    def multi_dropdown_hover_2(self, browser):
        action = ActionChains(browser)
        action.move_to_element(self.find(multiple_dropdown_hover_2)).perform()

    def multi_dropdown_menu_2_is_displayed(self):
        return self.find(multiple_dropdown_menu_2).is_displayed()

    def multi_dropdown_third_level(self):
        return self.find(multiple_dropdown_value_2).click()

    def multi_dropdown_hover_3(self, browser):
        action = ActionChains(browser)
        action.move_to_element(self.find(multiple_dropdown_hover_3)).perform()

    def multi_dropdown_menu_3_is_displayed(self):
        return self.find(multiple_dropdown_menu_3).is_displayed()

    def multi_dropdown_fourth_level(self):
        return self.find(multiple_dropdown_value_3).click()