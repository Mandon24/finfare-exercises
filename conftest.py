import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# modify params to include different configurations
# i.e. ["chrome-headless", "firefox-headless", "chrome", "firefox"]
@pytest.fixture(scope="session", params=["chrome"])
def driver(request):
    """
    Pytest fixture to initialize WebDriver with different configurations.
    Parametrized to pass in different browser configurations.
    """
    if request.param == "chrome-headless":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox-headless":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver
    driver.quit()
