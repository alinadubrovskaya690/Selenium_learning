from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

URL = 'https://qa-practice.netlify.app/alerts'

alert_btn = (By.XPATH, '//button[@id = "alert-btn"]')
confirm_btn = (By.XPATH, '//button[@id = "confirm-btn"]')

class AlertPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def alert_open(self):
        self.open(URL)

    def alert_button(self):
        return self.find(alert_btn).click()

    def confirm_button(self):
        return self.find(confirm_btn).click()