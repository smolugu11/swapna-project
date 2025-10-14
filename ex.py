# def add():
#     x =5
#     y = x+5
#     print(y)
# add()

def calculate_sum(y):
    x = 5
    result=x + y
    return result

print(calculate_sum(5))  # Output: 10
#  Step-by-Step Execution Flow
# - Function Definition (def calculate_sum(y):)
# - Python sees this and stores the function in memory.
# - It does NOT run anything inside the function yet.
# - Function Call (print(calculate_sum(5))) ← ✅ Execution starts here
# - This is the first line that actually runs.
# - Python calls calculate_sum(5) and passes y = 5.
# - Inside the Function:
# - x = 5 → Assigns 5 to variable x.
# - result = x + y → Adds x and y → 5 + 5 = 10.
# - return result → Sends back 10 to the caller.
# - Back to print(...)
# - print(10) → Displays the result.

def add_numbers(a,b):
        addition = a+b
        return addition
print(add_numbers(5,10))
# it store the function in memory . It calls the function add_numbers(5,10)
# then it# es a = 5 and b = 10 into the function.
# - Inside the function:
# - addition = 5 + 10 = 15
# - The function returns 15, which is printed.

def let(x):
    if x> 10:
        return "good"
    else:
        return "bad"
print(let(11))

def greetings(int):
    name = input("enter the number: ")
    return "hello Python"
print(greetings(int))

def greetings(num):
    name = input("enter the number: ")
    return "hello Python"

print(greetings(5))

def multple_print():
    num = int(input("enter the number: "))  # ✅ correct assignment
    for i in range(num):                   # ✅ use num here
        print("hello Python")

multple_print()
