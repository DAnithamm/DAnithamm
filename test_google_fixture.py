from selenium import webdriver
import pytest
import driver
import time
driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------setup-----")
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com/')
    yield
    print("------teardown----")
    driver.quit()

#def test_google_title(init_driver):
 #   assert driver.title == 'Google'
#def test_google_url(init_driver):
 #   assert driver.current_url == "https://www.google.com/"

# or
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == 'Google'

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/"





