import pytest
from selenium import webdriver
from page.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_wrong_password(driver):
    driver.get("https://signin.ebay.com")

    login_page = LoginPage(driver)
    login_page.enter_username("kristinesargsyants@gmail.com")
    login_page.enter_password("Whatever111")
    login_page.click_signin()

    error_message = "Oops, that's not a match."
    assert error_message in driver.page_source