import json
import os.path

import pytest

from src.fixture.application import Application

fixture = None
target = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as config_f:
            target = json.load(config_f)
    browser = request.config.getoption("--browser")
    fixture = Application(browser, target['baseUrl'])
    fixture.navigation.main_page()
    fixture.navigation.choose_country("United States")
    return fixture


@pytest.fixture(scope="session")
def stop(request):
    request.addfinalizer(fixture.tearDown)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
