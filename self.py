"""
# Class is a blueprint for creating objects. An object has properties and methods (functions) associated with it.
#instace variable: A variable that is defined inside a method and belongs to the object created from the class.
#class variable: A variable that is shared among all instances of a class. It is defined within the class but outside any methods.
"""

#self is a special variable used inside class methods in Python to refer to the current instance (object) of the class.
# It allows each object to keep track of its own data.
"""
Why Is self Important?
Distinguishes objects: When you create multiple instances (like person1 and person2), each object's data is kept separate via self.

Access instance variables: Using self, you can attach and access variables that belong only to the specific object.

Connects methods to the object: When you call a method (like eat()), self lets that method act on the calling object's data

Think of self like “this object.” If you have a room full of robots, each robot calls its own methods with its own data—self makes sure Robot A doesn't accidentally use Robot B's batteries!


"""
class Person():

# self is pre-defined variable, let you access the objects in class
    def __init__(self,name):
        # self._name = name  # instance variable
        self._name = name
        print(f"{name} is created")
        # print(id(self))

    def eat(self):
        print("Person can eat")

    def talk(self):
        print("Person can talk")

    def work(self):
        print("Person can work")

# now we will create an object of the class Person
def main():
    person1 = Person("Swapna") # create object of class Person. object first store in memory and its address is printed using id(self)
    person2 = Person("Zara")
    person1.eat()
    person1.talk()
    person2.talk()

    print(person1._name) # prints the name attribute of person1 object
    print(person2._name)
main() # calling the main function to execute the code

"""1. Python Will Treat the Method as a Regular Function
The method won’t be able to access instance variables or other methods.

You won’t have a way to refer to the object’s data.

2. Calling the Method Causes an Error
If you try to call the method from an object (e.g., obj.method()), Python always passes the instance as the first argument.

If self isn’t listed in the parameters, Python will throw a TypeError.

Example:
python
class Person:
    def wrong_method():  # Missing 'self'
        print("Hello!")

person = Person()
person.wrong_method()
Output:

text
TypeError: wrong_method() takes 0 positional arguments but 1 was given"""