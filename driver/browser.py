import contextlib
from typing import Generator, ContextManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from commons.settings import settings
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.chrome.options import Options


WebDrivers = ChromeDriver | FirefoxDriver


@contextlib.contextmanager
def chrome_driver() -> Generator[WebDrivers, None, None]:
    options = Options()
    # options.add_argument("--headless=new")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(executable_path=settings.path_chrome_driver)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.close()
