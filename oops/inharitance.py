class Testteam: #parents class or super class
    def emp1(self):
        print("Employee 1 is a Team lead")
    def emp2(self):
        print("Employee 2 is a Tester")

#   Inheritance: scrummaster class inherits from Testteam class. its a Child or sub class
class Scrummaster(Testteam):  # Inheritance: EmployeeDetails class inherits from Employee class. Child or sub class. Sub calss can access properties and methods of parent class but super class cannot access properties and methods of child class
    def emp3(self):
        print(("Employee 3 is a scrum master"))

e3 = Scrummaster() #you created an object of EmployeeDetails class
e3.emp1() #calling emp1 method of parent class using child class object
e3.emp3()
e3.emp2()

# above code called signle level inharitacne

class Manager(Scrummaster): # Multi level inheritance: Manager class inherits from Scrummaster class
    def emp4(self):
        print("Employee 4 is a Manager")
m1=Manager()
m1.emp1()
m1.emp3()
m1.emp4()

#multiple inheritance. Manager class is child, it inherits from Scrummaster(parent) class and which inherits from Testteam clasfff
"""In Python, inheritance lets you create a new class (called a child or derived class) that reuses the properties and methods of an existing class (the parent or base class). This makes your code more modular, organized, and easier to maintain by minimizing repetition."""

# multple inheritance is when are 3 classes, 3 rd class inherits from 1st and 2nd class. 2 parent class does not inherit from first class