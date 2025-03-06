from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    add_product1 = (By.XPATH, "//a[@data-product_id='160']")
    add_product2 = (By.XPATH, "//a[@data-product_id='163']")
    cart = (By.XPATH, "//a[@title='View your shopping cart']")
    removeItem = (By.XPATH, "//a[@data-product_id='160']")

    def addFirstItem(self):
        return self.driver.find_element(*CartPage.add_product1)

    def addSecondItem(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(CartPage.add_product2))

    def viewCart(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(CartPage.cart))

    def get_productDetails(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, ".shop_table .cart_item")
        product_details = []

        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, ".product-name a").text
            product_price = product.find_element(By.CSS_SELECTOR, ".product-price .amount").text
            product_quantity = product.find_element(By.CSS_SELECTOR, ".product-quantity .qty").get_attribute("value")

            product_info = {
                "name": product_name,
                "price": product_price,
                "quantity": product_quantity,
            }
            product_details.append(product_info)
        return product_details

    def removeCart_Item(self):
        return self.driver.find_element(*CartPage.removeItem)

