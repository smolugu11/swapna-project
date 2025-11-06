# dunder methods are --inti__, __str__, __add__, __sub__, __mul__, __truediv__, __len__, __getitem__, __setitem__, __delitem__, __iter__, __next__
"""
— encapsulation is a concept that applies only to class-level variables,
Encapsulation is part of object-oriented programming (OOP), and it works by:
- Defining attributes inside a class
- Controlling access using methods like getters and setters
- Hiding internal state from outside interference
Hiding internal data and exposing only what’s necessary through controlled access.
It helps you:
- Protect sensitive or critical data
- Prevent accidental or invalid changes
- Keep your code modular, clean, and maintainable

Global variables, on the other hand:
- Exist outside any class
- Are accessible from any part of the program
- Cannot be protected or validated using encapsulation

"""

class Student():
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.__age = age    # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, value):
        if 0 < value < 150:
            self.__age = value
            print(self.__age)
        else:
            print("Invalid age!")
# creating obj of    Student class
student1 = Student("John", 21)
print(student1.name)        # Accessing public attribute
student1.name = "Swapna Molugu" # we can change name directly easily and no condition
print(student1.name)        # Accessing modified public attribute
print(student1.get_age())   # Accessing private attribute via getter
student1.set_age(50)       # Modifying private attribute via setter
