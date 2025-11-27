from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

URL = 'https://qa-practice.netlify.app/pagination'

page_1_btn = (By.XPATH, '//a[text()="1"]')
page_1_alert = (By.XPATH, '//div[text()="You clicked page no. 1"]')
page_2_btn = (By.XPATH, '//a[text()="2"]')
page_2_alert = (By.XPATH, '//div[text()="You clicked page no. 2"]')
page_3_btn = (By.XPATH, '//a[text()="3"]')
page_3_alert = (By.XPATH, '//div[text()="You clicked page no. 3"]')
next_page_btn = (By.XPATH, '//a[text()="Next"]')
next_page_alert = (By.XPATH, '//div[@id="pageResult"]')

class PaginationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def pagination_open(self):
        self.open(URL)

    def page_1_button(self):
        return self.find(page_1_btn).click()

    def page_1_alert_is_displayed(self):
        return self.find(page_1_alert).is_displayed()

    def page_2_button(self):
        return self.find(page_2_btn).click()

    def page_2_alert_is_displayed(self):
        return self.find(page_2_alert).is_displayed()

    def page_3_button(self):
        return self.find(page_3_btn).click()

    def page_3_alert_is_displayed(self):
        return self.find(page_3_alert).is_displayed()

    def next_page_button(self):
        return self.find(next_page_btn).click()

    def next_page_alert_is_displayed(self):
        return self.find(next_page_alert).is_displayed()