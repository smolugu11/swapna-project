# - The function funct() is called.
# - A for loop runs from i = 0 to i = 4 (5 iterations).
# - On each iteration:
# - It prints "starting the loop X" where X is the current value of i.
# - It asks the user: "enter y/n to stop: "
# - If the user enters 'y', the loop breaks immediately.
# - If the user enters 'n' (or anything else), it prints "stopping the loop X" and continues.
# - After the loop ends (either by completing or breaking), it prints "loop stopped".


def funct():
    for i in range(5):
        print("starting the loop " + str(i))
        stop = input("enter y/n to stop: ")
        if stop == 'y':
            break # stop the loop and print statement in for loop not the print in the in if
        print ("stopping the loop " + str(i))
    print("loop stopped") # this will run
funct()