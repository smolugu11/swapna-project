

class Person():

# self is pre-defined variable, let you access the objects in class
    def __init__(self, name):
        self._name = name  # instance variable
        print(f"{self._name} is created")
        print(id(self))

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

    print(person1._name) # prints the name attribute of person1 object
    print(person2._name)
main() # calling the main function to execute the code