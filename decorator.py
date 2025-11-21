
"""
A decorator in Python is a special tool that lets you change or add to what a function does, without editing the function itself.
Think of it like gift wrapping— you can add a ribbon or note (extra features),
without changing the gift (the original function).
"""
def say_hello():
    print("Hello!")
def excited_decorator(func):
    def wrapper():
        print("I'm so excited!")
        func()
    return wrapper

decorated = excited_decorator(say_hello)
decorated()

