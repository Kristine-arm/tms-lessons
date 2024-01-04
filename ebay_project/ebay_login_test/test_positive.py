import pytest
from selenium import webdriver
from login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://signin.ebay.com")

    login_page = LoginPage(driver)
    login_page.enter_username("kristinesargsyants@gmail.com")
    login_page.enter_password("Ebay1111!")
    login_page.click_signin()

    assert "My eBay" in driver.title

