"""
In a pytest automation framework and in Python projects, __init__.py is a special file that tells Python to treat a directory as a package.

Key Roles of __init__.py in pytest and Python projects:
Makes a directory a Python package:
If a directory contains __init__.py, you can import modules from it using dot notation (e.g., from pages.login_page import LoginPage).

Allows test modules and helpers to be imported across your project:
This is especially useful in pytest, where you might have:

pages/
    __init__.py
    login_page.py
tests/
    __init__.py
    web/
        __init__.py
        test_login.py

"""