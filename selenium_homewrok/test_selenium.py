import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()

    def fin():
        # ** В конце теста можно делать скриншот страницы. Делается это через driver. save_screenshot()
        driver.save_screenshot(f"screenshot_{request.node.name}.png")
        driver.quit()

    request.addfinalizer(fin)
    return driver

class TestSelenium:
    #тест должен быть параметризированным. Т.е. должны быть две переменные url и page_title, которые меняются
    @pytest.mark.parametrize("url, expected_title", [
        ("https://www.amazon.com/", "Amazon"),
        ("https://www.apple.com/", "Apple"),
        ("https://www.google.com/", "Google")
    ])
    def test_website_titles(self, driver, url, expected_title):
        driver.get(url)
        actual_title = driver.title
        assert actual_title == expected_title, f"Title mismatch for {url}"