def func():
    PASSWORD = "hello"
    for i in range(3):
        userpassword = input("enter your passwrod: ")
        if userpassword == PASSWORD:
            print(" greetings Professror")
            break
        else:
            print("wrong password")
func()

