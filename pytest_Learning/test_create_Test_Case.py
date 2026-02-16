import pytest

def setup_module(module):
    print("Creating the DB Connection")

def teardown_module(module):
    print("Closing the DB Connection")

def setup_function(function):
    print("Launching the browser")

def teardown_function(function):
    print("Closing the browser")

def test_login():
    assert True
    print("Forcefully pass the testcase")

def test_registration():
    assert True
    print("Forcefully pass the testcase")