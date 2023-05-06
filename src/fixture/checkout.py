from selenium.webdriver.common.by import By

from src.model.item import Item


class CheckoutHelper:
    def __init__(self, app):
        self.app = app

    def get_item(self):
        wd = self.app.wd
        name = wd.find_element(By.CSS_SELECTOR, "section.card h2.cart-item__title-heading").text
        price = wd.find_element(By.CSS_SELECTOR, "section.card div.price-block__primary-price").text.replace("$", "")
        return Item(name=name, price=price)

    def get_gross_amount(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH,
                               "//div[contains(@class, 'below-the-line-item')]//div[position()=2]").text.replace("$",
                                                                                                                 "")

    def get_tax(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[@class='price-summary-line']//a/..//span").text.replace("$", "")
