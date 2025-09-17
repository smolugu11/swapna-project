#!C:\Users\navee\PycharmProjects\PythonProject\PythonProject\.venv\Scripts\python.exe

# this will print hello 5 times 0,1,2,3,4
for i in range(5):
    print("Hello " + str(i))
# this print hello 3 times 1,2,3 ( does not include 4)
for i in range(1, 4):
    print(i)


# it skips 2 and print 1 to 7 ( does not include 8)
for i in range(1, 8,2):
    print(i)

# HARDCODED PASSWORD CAN BE DEFINED AS A CONSTANT , excercise
PASSWORD = "HELLO"
for _ in range(3):
    password = input("Enter your password: ")
    if password == PASSWORD:
        print("Greeting Professor!")
        break # is the password is correct it will break the loop else the loop will continue till 3 attempts

    else:
        print("Access denied. Try again.")