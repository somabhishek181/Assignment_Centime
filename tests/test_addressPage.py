import pytest

from POMpages.AddressPage import AddressPage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("login_fixture")
class TestAddressPage(BaseClass):
    def test_billingAddress(self):
        log = self.getLoger()
        addressPage = AddressPage(self.driver)

        log.info("Navigating to the address Page.")
        self.driver.get("https://practice.automationtesting.in/my-account/")

        log.info("Clicking on the address button")
        addressPage.get_addressButton().click()

        log.info("Clicking on the Edit button for Billing Address.")
        addressPage.edit_billingAddress().click()

        log.info("Filling in the billing address details.")
        addressPage.enter_billing_details(
            first_name="Ashmit",
            last_name="Sood",
            company="ATT G",
            address1="Kesnand Road, Wagholi",
            address2="Rudra Apartments",
            city="Pune",
            postcode="412207",
            phone="1234567890"
        )

        log.info("Selecting the Country and State")
        # addressPage.select_country("India")
        # addressPage.select_state("Maharashtra")

        log.info("Save the address")
        addressPage.save_address()

        log.info("Verifying success message")
        success_msg = addressPage.get_success_message()
        assert "Address changed successfully" in success_msg, "Address save failed!"
        log.info("Address was saved successfully.")
