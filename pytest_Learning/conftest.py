import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def get_browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.w3schools.com/")
    print("Open the browser")
    yield driver
    driver.quit()
    print("Close the browser")
