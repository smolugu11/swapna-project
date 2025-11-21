#tehse are the units tests for math_func.py
"""
This is a Python module (file) designed specifically for testing the functions you wrote in math_func.py.

It should import functions from math_func and use assert statements or a test framework (like pytest) to check correctness.

Its only goal is to verify your code works as expected.
py test you no need to call a function to run the tests.

"""
import math_func


def test_add():
    # assert math_func.addition(1, 2) == 3
    assert math_func.add(1, 2) == 3


def test_sub():
    assert math_func.sub(2, 2) == 0

def test_add_string():
    result = math_func.add("hello", "world")
    assert result == "helloworld"
    assert type(result) == str
    assert 'heldoi' not in result



