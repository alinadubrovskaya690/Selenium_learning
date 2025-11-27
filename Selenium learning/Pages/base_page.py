from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, URL):
        self.browser.get(URL)

    def find(self, args):
        return self.browser.find_element(*args)