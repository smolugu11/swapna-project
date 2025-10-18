#anonymous function or lamda

def square(x):
    return x * x
print(square(5))

# instead of above

f = lambda x: x * x # anonymous function you no need to define it with def and return keyword you can directly return the value. you are assigning the function to a variable f
result = f(5)
print(result)

f =lambda x,y:x+y
result = f(5,5)
print(result)
