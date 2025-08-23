import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test_valid_login():
    driver.get('https://qa-practice.netlify.app/auth_ecommerce')
    email_field = driver.find_element(By.CSS_SELECTOR, '#email').send_keys('admin@admin.com')
    password_field = driver.find_element(By.CSS_SELECTOR, '#password').send_keys('admin123')
    submit_btn = driver.find_element(By.CSS_SELECTOR, '#submitLoginBtn').click()
    time.sleep(5)
    driver.quit()

