import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

@pytest.fixture(scope="function")
def driver():
    load_dotenv()

    username = os.getenv("LT_USERNAME")
    access_key = os.getenv("LT_ACCESS_KEY")

    lt_options = {
        "user": username,
        "accessKey": access_key,
        "build": "QA Hackathon Build",
        "name": "QA Hackathon Test",
        "platformName": "Windows 10",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "selenium_version": "4.0.0"
    }

    options = Options()
    options.set_capability('LT:Options', lt_options)

    driver = webdriver.Remote(
        command_executor="https://hub.lambdatest.com/wd/hub",
        options=options
    )

    yield driver
    driver.quit()
