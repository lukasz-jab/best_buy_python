from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class NavbarHelper:
    def __init__(self, app):
        self.app = app

    def search_item(self, item):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.top-nav input#gh-search-input")))
        sleep(1)
        wd.find_element(By.CSS_SELECTOR, "div.top-nav input#gh-search-input").send_keys(item)
        self.submit_search_btn()

    def submit_search_btn(self):
        wd = self.app.wd
        wait = self.app.wait
        self.app.helper_base.delete_survey_invite()
        wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.top-nav button.header-search-button[type='submit']")))
        wd.find_element(By.CSS_SELECTOR, "div.top-nav button.header-search-button[type='submit']").click()
