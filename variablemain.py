import calc

# we created a module named calc.py and we are using that module here in this main program
def funct1():
    print("hi from funct1")
    results=calc.add(10,5)
    print("Addition result from calc module: ", results)

def funct2():
    print("hi from funct2")

def main():
    funct1()
    funct2()
main()

