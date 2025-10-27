"""
MRO (Method Resolution Order):Defines the order Python follows to look up methods in a class hierarchy
It’s the rulebook for inheritance

The super constructor in Python refers to using the super() function to call the constructor (__init__ method) of a parent class from within a child class. It’s a key part of inheritance and helps you reuse and extend functionality without rewriting code.
What Does super() Do?
- It gives access to methods from a parent or superclass.
- Most commonly used to call the parent’s constructor (__init__) inside a child class.
- It follows Python’s Method Resolution Order (MRO) to determine which method to call next.
"""


class A:
    def __init__(self):
        print("Inside A init")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

class B:
    def __init__(self):
        print("Inside B init")

    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__() #it will call the init of class A because A is first in the order of inheritance and B is second whicch is according to MRO and will not call init of class B
        print("Inside C init")

c1= C()
c1.feature1()
c1.feature3()


