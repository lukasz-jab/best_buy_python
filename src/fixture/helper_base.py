from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class HelperBase:
    def __init__(self, app):
        self.app = app

    def is_element_present(self, by, element):
        wd = self.app.wd
        wd.implicitly_wait(3)
        try:
            wd.find_element(by, element)
            return True
        except NoSuchElementException:
            return False
        finally:
            wd.implicitly_wait(7)

    def delete_survey_invite(self):
        wd = self.app.wd
        if (self.is_element_present(By.CSS_SELECTOR, "div#survey_window button#survey_invite_no")):
            wd.find_element(By.CSS_SELECTOR, "div#survey_window button#survey_invite_no").click()
