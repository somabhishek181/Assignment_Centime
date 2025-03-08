import time
from urllib import request

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POMpages.AccountPage import AccountPage


@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    service_obj = Service("C:\\WebDrivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=options)
    request.cls.driver = driver
    driver.get("https://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print(driver.title)
    yield driver
    driver.quit()


@pytest.fixture
def login_fixture(setup, request):
    driver = setup
    logger = request.cls.getLoger()
    accountPage = AccountPage(driver, logger)
    # Perform login
    logger.info("Launching the Login Page.")
    driver.get("https://practice.automationtesting.in/my-account/")

    logger.info("Entering login credentials.")
    accountPage.enter_login_username().send_keys("testuser181@example.com")
    accountPage.enter_login_password().send_keys("Abhiss@1234")
    logger.info("Clicking on the login button.")
    accountPage.submit_login().click()
    logger.info("Login process complete.")

