#!C:\Users\navee\PycharmProjects\PythonProject\PythonProject\.venv\Scripts\python.exe


PASSWORD = "hello" # predefined hardcoded password

def greeting():
    print("welcome ! No unauthorized access allowed.")

def check_password():
    password = input("Enter your password: ")

    if password == PASSWORD:
        print("Access granted.")
    else :
        print("Access denied.")

def main():
    greeting()
    check_password()

main()