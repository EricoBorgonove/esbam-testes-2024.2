from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture

def driver ():
    driver = webdriver.Chrome()
    driver.implicitly_wait (200)
    yield driver
    driver.quit ()
    
def test_google_search (driver):
    driver.get ("https://www.google.com.br")
    search_box = driver.find_element (By.NAME, "q")
    search_term = "esbam"
    
    search_box.send_keys (search_term + Keys.RETURN)
    
    
    assert search_term in driver.title