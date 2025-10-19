from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


URL = 'https://qa-practice.netlify.app/auth_ecommerce'

email_field = (By.XPATH, '//*[@id = "email"]')
password_field = (By.XPATH, '//*[@id = "password"]')
submit_btn = (By.XPATH, '//*[@id = "submitLoginBtn"]')
main_page = (By.XPATH, '//*[@id = "prooood"]')
login_error = (By.XPATH, '//*[@class = "alert alert-danger"]')


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def login_open(self):
        self.open(URL)

    def login_email_enter(self, email):
        return self.find(email_field).send_keys(email)

    def login_password_enter(self, password):
        return self.find(password_field).send_keys(password)

    def login_confirm(self):
        return self.find(submit_btn).click()

    @property
    def login_main_page_is_displayed(self):
        return self.find(main_page).is_displayed()

    @property
    def message_is_displayed(self):
        return self.find(login_error).is_displayed()

    @property
    def message_text(self):
        return self.find(login_error).text

    def message_attributes(self):
        background_color = self.find(login_error).value_of_css_property('background-color')
        font_size = self.find(login_error).value_of_css_property('font-size')
        print(background_color, font_size)




