from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def main_page(self):
        self.app.wd.get("https://www.bestbuy.com")

    def choose_country(self, country):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='content']//div[@class='country-selection']//img[@alt='" + country + "']")))
        sleep(2)
        wd.find_element(
            By.XPATH, "//div[@class='content']//div[@class='country-selection']//img[@alt='" + country + "']").click()
