
class Car:
    wheals = 4  #class variable shared by all objects of Car class

    def __init__(self):
        self.color = "red"
        self.model = "Toyota"

c1=Car()
c2=Car()

c1.color = "blue" #changing the color of c1 object without interfering with c2 object
Car.wheals = 6  #changing the class variable wheals for all objects of Car class

print(c1.color , c1.wheals)
print(c1.model)
print(c2.color,c1.wheals)
print(c2.model)


