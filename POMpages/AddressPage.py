import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    address_button = (By.XPATH, "//a[normalize-space()='Addresses']")
    billing_edit = (By.CSS_SELECTOR, "a[href*='/my-account/edit-address/billing']")
    first_name = (By.CSS_SELECTOR, "#billing_first_name")
    last_name = (By.XPATH, "//input[@id='billing_last_name']")
    company_field = (By.CSS_SELECTOR, "#billing_company")
    billing_phone = (By.XPATH, "//input[@id='billing_phone']")
    address1_field = (By.XPATH, "//input[@id='billing_address_1']")
    address2_field = (By.CSS_SELECTOR, "#billing_address_2")
    billing_city = (By.CSS_SELECTOR, "#billing_city")
    postcode = (By.CSS_SELECTOR, "#billing_postcode")
    country_dropdown = (By.ID, "billing_country")
    state_dp = (By.ID, "billing_state")
    save_button = (By.XPATH, "//input[@name='save_address']")
    success_message = (By.CSS_SELECTOR, ".woocommerce-message")

    def get_addressButton(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(AddressPage.address_button))

    def edit_billingAddress(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*AddressPage.billing_edit)

    def enter_billing_details(self, first_name, last_name, company, phone, address1, address2, city, postcode):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.company_field).send_keys(company)
        self.driver.find_element(*self.address1_field).send_keys(address1)
        self.driver.find_element(*self.address2_field).send_keys(address2)
        self.driver.find_element(*self.billing_city).send_keys(city)
        self.driver.find_element(*self.postcode).send_keys(postcode)
        self.driver.find_element(*self.billing_phone).send_keys(phone)

    def save_address(self):
        return self.driver.find_element(*self.save_button).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)).text
