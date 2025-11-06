#function is a block of code that performs a specific task and can be reused.

def greet():
    print("hello world")
    print("good morning")
greet()

def add(a, b):
    return a + b

print(add(5,4))

def add_sub(a, b):
    c = a + b
    d = a-b
    return c, d

print(add_sub(5,4))


def even():
    number = 0
    for i in range(0,101,2):
        print(i)

even()