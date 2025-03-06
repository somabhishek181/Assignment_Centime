import logging
import time

from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:
    def __init__(self, driver, logger):
        self.logger = logger
        self.driver = driver

    # Locators for Registration
    reg_email = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    reg_submit = (By.XPATH, "//input[contains(@value, 'Register')]")
    reg_message = (By.CSS_SELECTOR, ".woocommerce-MyAccount-content")
    error_message = (By.CSS_SELECTOR, ".woocommerce-error")

    # Locators for Login
    username_field = (By.XPATH, "//input[@id='username']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_button = (By.CSS_SELECTOR, "input[value='Login']")

    def enter_email(self):
        return self.driver.find_element(*AccountPage.reg_email)

    def enter_password(self):
        return self.driver.find_element(*AccountPage.reg_password)

    def submit_registration(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            register_button = wait.until(EC.presence_of_element_located(AccountPage.reg_submit))
            self.driver.execute_script("arguments[0].scrollIntoView();", register_button)  # Scroll to the element
            ActionChains(self.driver).move_to_element(register_button).click().perform()
            return True
        except TimeoutException:
            self.logger.warning("TimeoutException: Registration button not found.")
            return False

    def get_registration_message(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            return wait.until(EC.visibility_of_element_located(AccountPage.reg_message))
        except TimeoutException:
            self.logger.warning("TimeoutException: Registration message not found.")
            return "No success message found"

    def enter_login_username(self):
        self.driver.implicitly_wait(30)
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(AccountPage.username_field))
        #return self.driver.find_element(*AccountPage.username_field)

    def enter_login_password(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(AccountPage.password_field))
        #return self.driver.find_element(*AccountPage.password_field)

    def submit_login(self):
        return self.driver.find_element(*AccountPage.login_button)
