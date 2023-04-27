import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'https://mvparts.by/'


@pytest.fixture
def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture()
def chromedriver_headless():
    chromeopt = Options()
    chromeopt.add_argument("--headless")
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeopt)
    chrome.get(base_url)
    chrome.maximize_window()
    yield chrome
    chrome.close()


@pytest.fixture()
def chromedriver_docker() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(base_url)
    yield driver
    driver.quit()
