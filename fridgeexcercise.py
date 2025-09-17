#!C:\Users\navee\PycharmProjects\PythonProject\PythonProject\.venv\Scripts\python.exe

#temp = 6

#temp = int(input("Enter the temp: "))

#if temp < 0 :
    #print("Fridge is too cold")
#elif temp <= 4:
    #print("Fridge is ok")

#elif temp < 6:
   # print("Fridge is too broken")
#else:
    #print("temp is not recognized")

temp = 6
temp = int(input("Enter the temp: "))

STATUS_BROKEN = "Fridge is broken"
STATUS_OK = "Fridge is ok"
STATUS_COLD = "Fridge is too cold"
STATUS_WARM = "Fridge is too warm"

status = STATUS_BROKEN
if temp < 0 :
    status = STATUS_COLD
elif temp <= 4:
    status = STATUS_OK
elif temp < 6:
    status = STATUS_WARM
print(status)