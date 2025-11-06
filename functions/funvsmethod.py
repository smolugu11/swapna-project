
"""A function is a block of code that performs a specific task and can be called by its name, independent from any object or class.
Functions are created outside of classes and do not require an object to be called. """

def student():
    print("Student can study")
    print("Student can play")
student()

""""""
class Calculator:
    """A method is a function that is associated with an object (or class).
     Methods are defined inside a class and always take the class instance (called self) or class itself (called cls) as their first parameter
."""
    def add(self, a,b):
        result = a + b
        return result
        # print("results :",result)

calc=Calculator()
print(calc.add(1,2))


