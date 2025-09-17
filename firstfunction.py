#!C:\Users\navee\PycharmProjects\PythonProject\PythonProject\.venv\Scripts\python.exe

def ask_user_status():

    response  = input("How are you : ")

    if response == "OK" or response == "ok":
        print("Good to hear that")
    else:
        print("oh no")

ask_user_status()
