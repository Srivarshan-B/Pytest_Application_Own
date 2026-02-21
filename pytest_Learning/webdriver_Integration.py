import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import xpaths
# from pytest_Learning.conftest import get_browser


def get_the_data_from_the_user():
    global driver
    return [
        ("srivarhsna@gmail.com", "oifjasofon"),
        ("dani@gmail.com", "ksfmlamf"),
        ("sam@gmail.com", "fjasofnwoo"),
        ("roh@gmail.com", "jfnlafnl"),
    ]


@pytest.fixture()
def logon_failure(request, get_browser):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="login_ss", attachment_type=AttachmentType.PNG)


# def setup_function(function):
#     global driver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.w3schools.com/")
#     print("Open the browser")
#
#
# def teardown_function(function):
#     driver.quit()
#     print("Closed the browser")


@pytest.mark.usefixtures("logon_failure")
@pytest.mark.parametrize("username, password", get_the_data_from_the_user())
def test_login(username, password, get_browser):
    driver = get_browser
    driver.find_element(By.XPATH, xpaths.sign_in).click()
    driver.find_element(By.XPATH, xpaths.emmail).send_keys(username)
    driver.find_element(By.XPATH, xpaths.pwd).send_keys(password)
    driver.find_element(By.XPATH, xpaths.visible).click()
    # assert 1 == 2
    # allure.attach(driver.get_screenshot_as_png(), name="login_ss", attachment_type=AttachmentType.PNG)
    # driver.find_element(By.XPATH, xpaths.button).click()
    print("Completed the login successfully")
