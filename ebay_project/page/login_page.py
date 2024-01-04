from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'userid')
        self.password_input = (By.XPATH, "//*[@id='pass']")
        self.signin_button = (By.ID, 'sgnBt')

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_signin(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.signin_button)).click()