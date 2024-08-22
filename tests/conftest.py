import json
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_WAIT_TIME = 2
DEFAULT_BROWSER = "chrome"
BASE_URL = "https://chatlog.onrender.com/"

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=DEFAULT_BROWSER)
    parser.addoption("--wait_time", action="store", default=DEFAULT_WAIT_TIME)

@pytest.fixture(scope="session")
def setup(pytestconfig):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("start-maximized")

    driver = WebDriver(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(pytestconfig.getoption('wait_time'))
    yield driver
    driver.quit()



