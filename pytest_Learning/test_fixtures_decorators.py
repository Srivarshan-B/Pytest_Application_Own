import pytest
from pytest import fixture

@pytest.fixture(scope="module")
def setup():
    print("Setting up the DB Connection")
    yield
    print("Quitting up the DB Connection")

@pytest.fixture(scope="function")
def before():
    print("launcing the browser before the test case")
    yield
    print("close the browser after the test case")

@pytest.mark.usefixtures("setup", "before")
def test_login():
    assert True
    print("Forcefully pass the testcase")

@pytest.mark.usefixtures("setup", "before")
def test_registration():
    assert True
    print("Forcefully pass the testcase")