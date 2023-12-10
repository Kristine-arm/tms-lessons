import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("whatever")
    with webdriver.Chrome(options) as driver:
        yield driver

def assert_element(driver, xpath, clickable=False, return_many=False):
    wait = WebDriverWait(driver, 20)
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

def hover_over_element(driver, xpath):
    element = assert_element(driver, xpath)
    ActionChains(driver).move_to_element(element).perform()

class TestSeleniumPageHomework:
        def test_selenium(self, driver):
        card_button_xpath = "//*[@href = '/cards']"
        red_card_button_xpath = "//*[contains(@title, 'Красная карта 2.0')]"
        input_phone_number_button_xpath = ("//*[@aria-label='Номер мобильного телефона']")
        submit_xpath = "//*[@type = 'submit']"
        identification_text_xpath = ("//*[contains(text(), 'Пройдите идентификацию')]")
        go_to_msi_button_xpath = "//*[contains(text(), 'Перейти в МСИ')]"

        driver.get("https://myfin.by/")

        hover_over_element(driver, card_button_xpath)
        click(driver, red_card_button_xpath)

        # Переключиться
        driver.switch_to.window(driver.window_handles[-1])

        input_field = assert_element(driver, input_phone_number_button_xpath, clickable=True)
        input_field.send_keys("299402265")

        click(driver, submit_xpath)

        identification_text = assert_element(driver, identification_text_xpath)
        go_to_msi_button = assert_element(driver, go_to_msi_button_xpath)

        assert identification_text.is_displayed()
        assert go_to_msi_button.is_displayed()


    ...
