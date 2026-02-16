import pytest

@pytest.mark.functinal
def test_login():
    assert True
    print("Forcefully pass the testcase")

@pytest.mark.dinosaur
def test_registration():
    a= "Dhoni"
    b= "Virat"
    if a==b:
        assert True
        print("Both string matched")
    else:
        print("Not Matched")
        assert False

@pytest.mark.regression
def test_logout():
    assert True
    print("Forcefully pass the testcase")

@pytest.mark.skip(reason="I don't want to run")
@pytest.mark.dinosaur
def test_skip():
    assert True
    print("Forcefully pass the testcase")

