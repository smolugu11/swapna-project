#static methhods are used to define functions that are not bound to an instance of a class.
# They can be called on the class itself without creating an instance.

class Student:
    school = "Molugu High School"  # class variable

    def __init__(self, m1,m2,m3):
        self.m1 = m1 # instance variable
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,m1):
        self.m1 = m1 # setter method to set the value of m1

    @classmethod
    def getSchool(cls):
        return cls.school # accessing class variable using cls parameter

    @staticmethod
    def info():
        return "This is Student class which is used to create student objects"

s1 = Student(34,56,67)
s2 = Student(88,45,78)

s1.average()
print(s1.average())
print(s2.average())
print(Student.getSchool())  # calling class method without creating an instance

"""Key Differences
@classmethod methods receive the class itself (cls) and can alter class-wide or shared data. Useful for creating alternate constructors or managing class-level resources.

@staticmethod methods don’t receive any special argument. They’re just regular functions grouped within the class for logical reasons—used for operations that don’t need class or object data.

Simple Rule of Thumb
Use @classmethod when you want a method that deals with the class as a whole.

Use @staticmethod for grouped utility logic that neither needs instance nor class context.

This distinction will help keep your code structured and idiomatic, especially in OOP and interview situations."""