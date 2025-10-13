import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    service = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=service)
    return chrome