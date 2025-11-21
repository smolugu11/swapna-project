import pytest
"""
Below markers(cusotm) are you created and its not default so you have to save them in pytest.ini file. you can use to run pytest .\test_markers.py -m smoke

when you run the marker file, it gives you warming to you can register by created pytest.ini file and add the markers. checkout pytest.ini

s this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smoke

"""

@pytest.mark.smoke #created a new marker of your own
def test_login():
    print("Testing login")

@pytest.mark.regression
def test_addproduct():
    print("Testing add product")

@pytest.mark.smoke
def test_logout():
    print("Testing logout")

