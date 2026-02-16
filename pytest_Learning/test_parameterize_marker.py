import pytest

def get_the_data_from_the_user():
    return [
        ("srivarhsna", "oifjasofon"),
        ("dani", "ksfmlamf"),
        ("sam", "fjasofnwoo"),
        ("roh", "jfnlafnl"),
        ]

@pytest.mark.parametrize("username, password", get_the_data_from_the_user())
def test_login_info(username, password):
    print("login info")
    print(username, "---------" ,password)