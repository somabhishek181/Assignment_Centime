import time

import pytest

from POMpages.CartPage import CartPage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestCartPage(BaseClass):
    def test_CartPage(self):
        log = self.getLoger()
        cartPage = CartPage(self.driver)

        log.info("Adding the first item to the cart.")
        cartPage.addFirstItem().click()

        time.sleep(5)
        log.info("Adding the second item to the cart.")
        cartPage.addSecondItem().click()

        cartPage.viewCart().click()
        log.info("Navigating to the cart page.")

        log.info("Retrieving product details from the cart.")
        product_details = cartPage.get_productDetails()
        log.info(f"Product Details in Cart: {product_details}".encode('utf-8'))

        assert len(product_details) == 2, "Not all items were added to the cart."

    def test_removeItems_Cart(self):
        log = self.getLoger()
        cartPage = CartPage(self.driver)

        log.info("Clicking on the Remove Item button.")
        cartPage.removeCart_Item().click()
        log.info("Item removed from the cart.")

        log.info("Retrieving product details from the cart after remove item.")
        product_details = cartPage.get_productDetails()
        log.info(f"Product Details in Cart: {product_details}".encode('utf-8'))


