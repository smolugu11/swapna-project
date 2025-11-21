class A:
    def __init__(self):
        print("Inside A init")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

class B(A):
    def __init__(self):
        super().__init__() #it will call the init of class A when we use super() else it just call init of class B
        print("Inside B init")
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

b1=B() # when we create object of class B, it will call init of class B and also init of class A because of super(). it will call init of B first then it executes init of A and then
b1.feature1()
b1.feature3()
b1.feature2()
"""
The __init__ method in class A is the constructor. It initializes objects of class A and prints "Inside A init" when an object is created. In inheritance, when you create an object of class B, calling super().__init__() in B's constructor ensures that A's constructor runs, allowing any setup in A to happen for B objects as well. This is important for proper initialization in the inheritance chain.

"""