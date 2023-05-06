from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.model.item import Item


class DetailPageHelper:
    def __init__(self, app):
        self.app = app

    def get_item(self):
        wd = self.app.wd
        name = wd.find_element(By.CSS_SELECTOR, "div.shop-product-title div[itemprop='name'] h1").text
        model = wd.find_element(By.CSS_SELECTOR, "div.shop-product-title span.product-data-value.body-copy").text.replace(" ", "")
        price = wd.find_element(By.CSS_SELECTOR,
                                "div.container-v3 div.priceView-layout-large div.priceView-customer-price span[aria-hidden='true']") \
            .text.replace("$", "")
        return Item(name=name, model=model, price=price)

    def add_to_cart(self):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "div[id^='fulfillment-add-to-cart-button'] button[data-button-state='ADD_TO_CART']")))
        wd.find_element(By.CSS_SELECTOR,
                        "div[id^='fulfillment-add-to-cart-button'] button[data-button-state='ADD_TO_CART']").click()

    def go_to_cart(self):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.c-modal-grid div.go-to-cart-button a")))
        wd.find_element(By.CSS_SELECTOR, "div.c-modal-grid div.go-to-cart-button a").click()
