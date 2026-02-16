import pytest
from pytest_check import check
from tabulate import tabulate

errors = []

def soft_assert(name, actual, expected):
    if actual != expected:
        errors.append([name, actual, expected])



def test_login():
    # expected_result = ''
    # actual_result = ''
    thanthuvem = 'Silence is the most powerful'
    # check.equal(expected_result,actual_result)
    # check.is_in("Kill",thanthuvem)
    soft_assert("Check 1", "Vazhai oru otagam nondi ottagam", "Vazhai oru otagam nondi")
    soft_assert("Check 2", 3, 4)
    soft_assert("Check 3", 5, 0)
    soft_assert("Check Word", "Kill", thanthuvem)


    if errors:
        print("\nAssertion Report:\n")
        print(tabulate(errors, headers=["Test", "Actual", "Expected"], tablefmt="grid"))
        assert False
