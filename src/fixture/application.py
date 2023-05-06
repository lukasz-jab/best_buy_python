from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.fixture.checkout import CheckoutHelper
from src.fixture.detail_page import DetailPageHelper
from src.fixture.helper_base import HelperBase
from src.fixture.navbar import NavbarHelper
from src.fixture.navigation import NavigationHelper
from src.fixture.search_page import SearchPageHelper


class Application:
    def __init__(self, browser, baseUrl):
        self.browser = browser
        self.baseUrl = baseUrl
        if self.browser == "chrome":
            self.wd = webdriver.Chrome()
        if self.browser == "firefox":
            self.wd = webdriver.Firefox()
        self.wd.maximize_window()
        self.wd.implicitly_wait(7)
        self.wait = WebDriverWait(self.wd, timeout=5)
        self.navigation = NavigationHelper(self)
        self.nav = NavbarHelper(self)
        self.search_result = SearchPageHelper(self)
        self.helper_base = HelperBase(self)
        self.detail = DetailPageHelper(self)
        self.checkout = CheckoutHelper(self)

    def tearDown(self):
        self.wd.quit()
