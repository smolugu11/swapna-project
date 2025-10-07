#!C:\Users\navee\PycharmProjects\PythonProject\PythonProject\.venv\Scripts\python.exe

def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper