from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

URL = 'https://qa-practice.netlify.app/file-upload'

choose_file_btn = (By.XPATH, '//input[@id = "file_upload"]')
submit_btn = (By.XPATH, '//button[@type = "submit"]')
submit_alert = (By.XPATH, '//div[@id = "file_upload_response"]')

class FileUploadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def file_upload_open(self):
        self.open(URL)

    def choose_file_button(self, upload_file_path):
        return self.find(choose_file_btn).send_keys(upload_file_path)

    def submit_button(self):
        return self.find(submit_btn).click()

    def submit_alert_is_displayed(self):
        return self.find(submit_alert).is_displayed()

    def submit_alert_text(self):
        return self.find(submit_alert).text