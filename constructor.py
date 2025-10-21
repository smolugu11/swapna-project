

class Person():

# Inti is a constructor in python
# add person function (method) like eat, talk, work is method. Which is a function inside a class.
# It defines what the object can do.You call a method on an object
    def __init__(self, name):

        print(f"{name} is created")

    def eat(self):
        print("Person can eat")

    def talk(self):
        print("Person can talk")

    def work(self):
        print("Person can work")

# now we will create an object of the class Person
def main():
    person1 = Person("Swapna")
    person2 = Person("Zara")
    person1.eat()
    person2.talk()
main() # calling the main function to execute the code