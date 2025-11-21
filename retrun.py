

def greet(name):                  # Define a function that prints "hello" + name
    print("hello " + name)        # Executes when greet() is called

def create_greeting(name):        #  4: Define a function that returns "hi" + name
    return "hi " + name           # Line 5: Executes when create_greeting() is called
#- It sends a value back to wherever the function was called.
def main():
    name = "john"                 # Line 3: Python enters the main() functionSet variable 'name' to "john"
    greet(name)                   # Line 4: Call greet() → prints "hello john"
    greeting = create_greeting(name)  # Line 5: Call create_greeting() → returns "hi john"
    print(greeting)               # Line 6: Print the returned greeting → "hi john"

main()                            # Line 2: Start the program by calling main()
#hello john
# hi john