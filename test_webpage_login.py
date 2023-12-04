from selenium import webdriver
import pytest
import driver
import time
driver = None
def setup_module(module):
    global driver
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com/')
def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == 'Google'
def test_google_url():
    assert driver.current_url == "https://www.google.com/"






