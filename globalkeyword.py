a=10 #global variable
print(a)
def func():
     x =5 #local variable
     print(x)
     global a # declare that we are using globla x variable
     a = a+5 ## tells Python to use the global 'a'

     print("inside the function :",a)
func()
print("outside the function :", a)