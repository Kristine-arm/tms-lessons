import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    with webdriver.Chrome(options=options) as driver:
        yield driver

class TestClass:
    def test_selenium_locators(self, driver):
        driver.get('https://www.thesaurus.com/')

        our_first_element = driver.find_element(By.XPATH, "//*[@id='global-search']")
        our_first_element.send_keys("love")

        wait = WebDriverWait(driver, 10)
        find_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='SFL_CJwX_oOmq1DF63xo']")))
        find_button.click()

        synonyms_elements = driver.find_elements(By.XPATH, "//*[@data-linkid='y2woe7']//span[@class='css-133coio etbu2a31']")
        synonyms = [element.text for element in synonyms_elements[:6]]

        print("6 synonyms of the word 'love':")
        for index, synonym in enumerate(synonyms, start=1):
            print(f"{index}. {synonym}")
