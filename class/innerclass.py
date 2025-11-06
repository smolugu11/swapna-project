"""An inner class (also called a nested class) in Python is a class defined inside another class.

It is written inside the body of another class, rather than at the top level of your module or script.

You access it as OuterClass.InnerClass.

Why use an inner class?
Encapsulation: It lets you logically group classes that are only used in one place.

Organization: Keeps your code tidy—helper classes that support the parent class stay hidden inside it.

Relationship: Signals a close functional or structural link between the parent and inner class.

Example
python
class Outer:
    class Inner:
        def greet(self):
            print("Hello from inner class!")
Here, Inner is an inner class inside Outer. To use it:
obj = Outer.Inner()

In summary:
An inner class is a class defined inside another to show tight coupling, provide better organization, or encapsulate logic that only belongs in the parent class.
"""


class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop("Dell", "i5")

    def show(self):
        print("hi,", self.name, self.rollno)
        lap = self.Laptop("Dell", "i5")

    class Laptop:
        def __init__(self, brand, cpu):
            self.brand = brand
            self.cpu = cpu

        def show(self):
            print("Laptop brand:", self.brand, "CPU:", self.cpu)


s1 =Student('Swapna',101)
s2=Student('Zara',10)
s1.show()
s2.show()
s1.lap.show()
