import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import expected_conditions as EC

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome("")
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    driver.quit()
