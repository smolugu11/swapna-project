import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Testing login")

@pytest.mark.skipif(sys.version_info< (3,11), reason="requires python3.12 or higher")
def test_addproduct():
    print("Testing add product")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Testing logout")