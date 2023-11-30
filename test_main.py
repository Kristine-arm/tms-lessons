import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
    with webdriver.Chrome() as driver:
        yield driver
    ...
    # driver = webdriver.Chrome()
    #return webdriver.Chrome()


class TestSelenium:
    def test_selenium_first(self):
        #Arrange
        #driver = webdriver.Chrome()

        # Act
        driver.get("https://www.python.org/")
        current_url= driver.current_url
        page_title = driver.title
        ...

        #   Assert n
        assert "python" in current_url


    def test_selenium_second(self):
        #Arrange
        driver = webdriver.Chrome()

        # Act
        driver.get("https://www.python.org/downloads")
        current_url= driver.current_url

        # Assert
        assert "downloads" in current_url
