from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from src.model.item import Item


class SearchPageHelper:
    def __init__(self, app):
        self.app = app

    def get_items(self):
        wd = self.app.wd
        wait = self.app.wait
        items = []
        wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div#main-results div.shop-sku-list-item")))
        itemsWE = wd.find_elements(By.CSS_SELECTOR, "div#main-results div.shop-sku-list-item")
        for item in itemsWE:
            name = item.find_element(By.CSS_SELECTOR, "div.column-middle h4 a").text
            link = item.find_element(By.CSS_SELECTOR, "div.column-middle h4 a").get_attribute("href")
            model = item.find_element(
                By.CSS_SELECTOR, "div.column-middle div.variation-info div.sku-attribute-title").text \
                .replace("Model:", "").replace(" ", "")
            price = item.find_element(By.CSS_SELECTOR,
                                      "div.column-right div.sku-list-item-price div.priceView-customer-price span[aria-hidden='true']") \
                .text.replace("$", "")
            items.append(Item(name=name, model=model, price=price, link=link))
        return items

    def sort_items(self, select):
        wd = self.app.wd
        self.app.helper_base.delete_survey_invite()
        sortSelect = Select(wd.find_element(By.CSS_SELECTOR, "label.sort-by-label select#sort-by-select"))
        sortSelect.select_by_visible_text(select)
        sleep(5)

    def open_item(self, item):
        wd = self.app.wd
        wd.get(item.link)
