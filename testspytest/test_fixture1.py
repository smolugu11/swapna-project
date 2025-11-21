"""
imagine you have a test , inside it can be multiple steps as below
Precondtion: setup, conenction , API
Test
Test
Aseertion
Postcondition: disconnect,clean,  close connection
We can use fixture to handle pre and post conditions . instead of writing this for each and every test , we can use fixture, we can define the scope.
 pytest .\test_fixture.py -s

"""

import pytest

@pytest.fixture
def setup(): #fixture function
    print("start the broswer")
    yield # anythong after yield is post condition
    print("close the browser")
def test_1(setup):# using the fixture

    print("This is test 1")

def test_2(setup):

    print("This is test 2")


def test_3(setup):
    print("This is test 3")
