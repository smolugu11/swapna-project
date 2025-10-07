class Person():

# add person function (method) like eat, talk, work is method. Which is a function inside a class. It defines what the object can do.You call a method on an object
    def eat(self):
        print("Person can eat")

    def talk(self):
        print("Person can talk")

    def work(self):
        print("Person can work")

#above code is the blue print for creating a person object .
# An object is a specific instance of a class. Think of it as a real person created from the blueprint (Person class).You can create multiple objects from the same class.

# now we will create an object of the class Person
def main():
    person1 = Person()  # creating an object of the class Person
    person2 = Person() # creating another object of the class Person
    person1.eat() # calling the eat method on person1 object
    person2.talk()
main() # calling the main function to execute the code

# - Class = Blueprint
# - Object = House built from blueprint
# - Method = Actions the house can perform (open door, turn on lights)
