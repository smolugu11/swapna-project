def funct():
    for i in range(5):
        print(" starting the loop " + str(i))
        stop = input("enter y/n to stop: ")
        if stop == 'y':
            continue #it skip rest of the code in the current loop iteration and moves to the next iteration.
        print(" stopping the loop " + str(i))
    print(" loop stopped")
funct()
# #🔁 continue: Skip the current iteration
# - What it does: Skips the rest of the code in the current loop iteration and moves to the next iteration.
# - Use case: When you want to ignore certain values but keep looping.
