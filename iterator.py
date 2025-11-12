# ex of iterators in python is list , which can be iterable

class PowersOfTwo:
    def __iter__(self):
        return self

#In Python, the __next__() method is part of the iterator protocol. It defines how an object returns the next item in a sequence when you're looping through it.

    def __next__(self):
        return 1

pot = PowersOfTwo() # creating an instance of the class
for i in pot: # iterating through the instance
    print(i)

