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


