#!C:\Users\navee\PycharmProjects\PythonProject\PythonProject\.venv\Scripts\python.exe

worker1 = "Sapna"
worker2 = "Naveen"
professor = "Aadhya"

name = input("Enter your name: ")

if name == worker1:
    print("Hello, Sapna")
elif name == worker2:
    print("hello, Naveen")
elif name == professor:
    print("hello, Aadhya")

else:
    print("Name is not recognized")