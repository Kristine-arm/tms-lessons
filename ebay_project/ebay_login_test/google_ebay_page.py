from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleHomePage:
    search_box = (By.NAME, 'q')

    def __init__(self, driver):
        self.driver = driver

    def search_for(self, keyword):
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box))
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.submit()


class EbaySearchResultsPage:
    ebay_link = (By.XPATH, "//a[contains(@href, 'ebay.com')]")

    def __init__(self, driver):
        self.driver = driver

    def click_ebay_link(self):
        ebay_link_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ebay_link))
        ebay_link_element.click()


class EbayLoginPage:
    sign_in_link = (By.LINK_TEXT, 'Sign in')
    email_input = (By.ID, 'userid')
    password_input = (By.ID, 'pass')
    sign_in_button = (By.ID, 'sgnBt')

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        sign_in_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sign_in_link))
        sign_in_element.click()

    def login(self, email, password):
        email_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input))
        password_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input))

        email_element.clear()
        email_element.send_keys(email)

        password_element.clear()
        password_element.send_keys(password)

        sign_in_button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sign_in_button))
        sign_in_button_element.click()