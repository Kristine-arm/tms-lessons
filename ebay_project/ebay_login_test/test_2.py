import pytest
from selenium import webdriver
from pages import GoogleHomePage, EbaySearchResultsPage, EbayLoginPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_ebay_login(browser):
    google_home_page = GoogleHomePage(browser)
    google_home_page.driver.get("https://www.google.com")
    google_home_page.search_for("ebay")

    ebay_search_results_page = EbaySearchResultsPage(browser)
    ebay_search_results_page.click_ebay_link()

    ebay_login_page = EbayLoginPage(browser)
    ebay_login_page.click_sign_in()
    ebay_login_page.login("your_email@example.com", "your_password")

