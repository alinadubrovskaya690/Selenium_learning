from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

URL = 'https://qa-practice.netlify.app/iframe'

iframe = (By.ID, 'iframe-checkboxes')
navbar_btn = (By.XPATH, '//a[@class = "navbar-brand"]')
burger_btn = (By.XPATH, '//button[@class = "navbar-toggler"]')
home_btn = (By.XPATH, '//a[text() = "Home "]')
features_btn = (By.XPATH, '//a[text() = "Features"]')
pricing_btn = (By.XPATH, '//a[text() = "Pricing"]')
disabled_btn = (By.XPATH, '//a[text() = "Disabled"]')
learn_more_btn = (By.XPATH, '//a[@id = "learn-more"]')
learn_more_text = (By.XPATH, '//div[@id = "show-text"]')

class IframePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def iframe_open(self):
        self.open(URL)

    def iframe_switch(self):
        return self.switch_to.frame(iframe)

    def navbar_button(self):
        return self.find(navbar_btn).click()

    def burger_button(self):
        return self.find(burger_btn).click()

    def home_button_is_displayed(self):
        return self.find(home_btn).is_displayed()

    def home_button(self):
        return self.find(home_btn).click()

    def features_button_is_displayed(self):
        return self.find(features_btn).is_displayed()

    def features_button(self):
        return self.find(features_btn).click()

    def pricing_button_is_displayed(self):
        return self.find(pricing_btn).is_displayed()

    def pricing_button(self):
        return self.find(pricing_btn).click()

    def disabled_button_is_displayed(self):
        return self.find(disabled_btn).is_displayed()

    def learn_more_button(self):
        return self.find(learn_more_btn).click()

    def learn_more_text_is_displayed(self):
        return self.find(learn_more_text).is_displayed()

    def learn_more_text(self):
        return self.find(learn_more_text).text