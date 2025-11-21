import pytest
import sys

"""
@pytest.mark.parametrize("arg1, arg2, ..., argN", [
    (val1_1, val2_1, ..., valN_1),
    (val1_2, val2_2, ..., valN_2),
    ...
])
def test_function(arg1, arg2, ..., argN):
    # test logic using arg1, arg2, ..., argN
    
ex: @pytest.mark.parametrize("x, y", [(1, 2), (3, 4)])
def test_addition(x, y):
    assert x + y > 0


"""
@pytest.mark.parametrize("username, password", [
    ("Selenium", "WebDriver"),
    ("Python", "Pytest"),
    ("Swapna","Test"),
    ("API","Automation")
])
def test_login(username, password):
    print(username)
    print(password)

#the programes run 4 times with 4 parameters