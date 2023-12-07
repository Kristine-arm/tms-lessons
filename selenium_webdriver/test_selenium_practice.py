import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument ("whatever")
    with webdriver.Chrome(options) as driver:
        yield driver

def assert_element(driver, xpath, clickable=False, return_many=False):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    if clickable:
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    if return_many:
        result = driver.find_elements(By.XPATH, xpath)
    else:
        result = driver.find_element(By.XPATH, xpath)

    return result
def click(driver, xpath):
    element = assert_element(driver, xpath, clickable=True)

    element.click()

class TestSeleniumThirdPractice:
    def test_selenium(self, driver):
    # 1: to open ebay.com page
    # 2: now to write in search window in ebay the word bager, therefore need to find locator
        input_xpath = "//*[@id= 'gh-ac']"
        search_button_xpath = "//*[@id = 'gh-btn']"
        second_image_xpath = "(//ul[@class='srp-results srp-list clearfix']//li)[2]//img"
        buy_button_xpath = "//*[@class='ux-call-to-action__text']"

        driver.get("https://www.ebay.com/")

        input_field = assert_element(driver, input_xpath)
        #3: now need to write ex word bager in the search place
        input_field.send_keys("bager")
        #now we need to pres enter button, therefore need to find locator
        #now select the second object in the new opened page
        click(driver, search_button_xpath)

        click(driver,second_image_xpath)
        #now when we know the second object, we need to click on that
        ...

        #now we need to go to another tab

        driver.switch_to.window(driver.window_handles[-1])
        #now in the new page we have the product, with buttons buy now, add to cart.. we need to click one of them
        #so for that we find locators of that buttons
        buy_buttons = assert_element(driver, buy_button_xpath, return_many=True)
        for buy_button in buy_buttons:
            print(buy_button.text)

