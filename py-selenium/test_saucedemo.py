import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.ui import expected_conditions as EC

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome("")
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_login(setup_browser):
    driver = setup_browser
    #mapeando os elementos
    username = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID,"login-button")
    # carregando o conetudo dos elementos
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    
    assert "inventory.html" in driver.current_url # procura o termo dentro da url
    assert "ADD TO CART" in driver.page_source # procura o termo na página
    assert "Products" in driver.page_source 
    
def test_login_blocked(setup_browser):
    driver = setup_browser
    #mapeando os elementos
    username = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID,"login-button")
    # carregando o conetudo dos elementos
    username.send_keys("locked_out_user")
    password.send_keys("secret_sauce")
    login_button.click()
    
    #assert "index" in driver.current_url # procura o termo dentro da url
    assert "Epic sadface: Sorry, this user has been locked out." in driver.page_source # procura o termo na página