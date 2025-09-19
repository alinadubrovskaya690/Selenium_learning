import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test_dropdown():
    driver.get('https://qa-practice.netlify.app/dropdowns')
    simple_dropdown = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown-menu'))
    simple_dropdown.select_by_index(2)
    time.sleep(15)
    driver.quit()