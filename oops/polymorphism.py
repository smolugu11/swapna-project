class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Penguin(Bird):
    def temo(self):
        pass
    # def flight(self):
    #     print("Penguins cannot fly.")

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_penguin = Penguin()

for bird in (obj_bird, obj_sparrow, obj_penguin):
    bird.intro()
    bird.flight()

"""
1.We'll start with a simple base class(super class) called Bird.Here we define a general Bird class with two methods — one introduces the concept, and the other talks about flight.

2.Create a child(sub) classes Sparrow and Penguin that inherit from Bird.Each child class has its own version of flight(), providing behavior specific to that type of bird.

3. Demonstrate Polymorphism We’ll create objects from each class and call their methods using the same interface

4. Underastanding Polymorphism:Here, all classes — Bird, Sparrow, and Penguin — share the same method name flight(), but their behavior changes depending on the object type. Python uses the correct version automatically at runtime.

Python uses the correct version automatically at runtime.

"""
