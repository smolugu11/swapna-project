import pytest
import sourcepytest.my_func as my_func


def test_add():
    assert my_func.add(2,6) == 8


def test_add_string():
    assert my_func.add("hello ", "world") == "hello world"

def test_sub():
    assert  my_func.sub(2, 2) == 0

def test_divide_by_zero():
    #result = my_func.divide(10, 0) #raise 0 division error and test failes
    # assert True
    with pytest.raises(ZeroDivisionError):
        my_func.divide(10, 0)


