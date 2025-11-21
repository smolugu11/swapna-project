""" 3 diffrent typees of error 1. syntax error( spell , missing colon) 2. logical error(when the code is right but logic  is wrong)
3. runtime error(( code get run, all good 2/2 good, 2/0 zerodviison) the mistake is run by user)
""""
"""The try…except…finally statement in Python is a control flow structure that lets you handle exceptions and guarantee the execution of cleanup logic.
The code inside the try block runs first. If an error occurs, Python skips to the except block.
Regardless of what happens — success, failure, or interruption — the finally block always runs"""

def func(x,y):
    try: #try: This block contains code that might throw an exception.
        result = x / y
        print("result: ", result)
    except ZeroDivisionError: #except: This block handles the exception if one occurs.
        print("Error: division by zero")
    finally: #finally: This block always executes, regardless of whether an exception occurred or not.
        print("this block always executes")


func(4,2)
func(4,0)

#open a file and read its contents
def read_file():
    try:
        file = open("data.txt", "r") #- Tries to open a file named data.txt in read mode ("r"). If the file doesn’t exist, this line will raise a FileNotFoundError

        content = file.read() # If the file opens successfully, it reads the entire content of the file into the variable content.
    except FileNotFoundError:    # If a FileNotFoundError occurs (i.e., the file doesn’t exist), the code jumps to this except block.
        print("Error: The file was not found.") # It prints an error message indicating that
    finally:
        print("closing file")
        file.close() # This line ensures that the file is closed after the operations are complete, regardless of whether an error occurred or not.


def number():
    try:
        items =[1,2,3]
        print(items[5])
    except Exception as e: #
        print("error is ", e) #In Python, except Exception as e: is used to catch and handle most runtime errors.

    finally:
        print("always run")
number()

"""In Python, runtime errors—also known as exceptions—occur during program execution and can disrupt the normal flow if not properly handled. 
These include a wide range of issues such as IndexError, which happens when accessing an invalid index in a list; KeyError, 
when trying to access a missing key in a dictionary; and ValueError, which arises when a function receives an argument of the correct type but 
inappropriate value. TypeError is common when operations are performed on incompatible data types, while ZeroDivisionError occurs when dividing by zero. 
File-related errors like FileNotFoundError, PermissionError, and IOError are triggered during file access problems.
 AttributeError is raised when referencing an undefined object attribute, and NameError when using an undefined variable.
  Other notable exceptions include ImportError, ModuleNotFoundError, RuntimeError, MemoryError, RecursionError, and TimeoutError. 
  All these exceptions inherit from the base class Exception, making them catchable using a generic except Exception as e: block. 
  However, system-level exceptions like KeyboardInterrupt and SystemExit inherit from BaseException and are not caught by this generic handler. 
  Proper exception handling ensures robust, crash-resistant code and improves user experience.
"""