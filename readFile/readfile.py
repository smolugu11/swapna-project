def main():

    """This function demonstrates how to read a file line by line and print its contents to the console"""
    """  try:
        file = open("if.py") #Open the file in read mode
        #read lines from the files
        lines = file.readlines() #  Step 2: Read all lines into a list

        for line in lines:   # Step 3: Loop through each line

            print(line , end="") ## Step 4: Print each line and end="" get rid of extra blanks

    finally:
        file.close() #clsoe the file # if there is an expection when you try to close it"""

"""Python’s recommended approach is using with, which handles opening and closing automatically—even during exceptions:
"""
#WITH statement

try:
    with open("if.py") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")
except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error reading the file.")

"""- The file is opened at with open("if.py") as file:
- Python reads all lines and prints them
- Once the loop finishes, Python automatically closes the fil
This reads line-by-line without loading the entire file into memory, which is better for large files
try and except blocks handle potential errors like file not found or read issues

# 📂 Common File Handling Exceptions in Python

# FileNotFoundError: Raised when the file or directory does not exist
# PermissionError: Raised when the program lacks permission to access the file
# IsADirectoryError: Raised when a directory is accessed like a file
# IOError / OSError: General input/output errors (e.g., disk issues, corrupted files)
# UnsupportedOperation: Raised when an invalid operation is performed on a file (e.g., write on read-only)
# ValueError: Raised when an invalid argument is passed (e.g., wrong mode in open())
# UnicodeDecodeError: Raised when decoding fails due to encoding mismatch
# FileExistsError: Raised when trying to create a file or folder that already exists
# EOFError: Raised when reading past the end of a file (e.g., input() with no data)

# ✅ Best Practice: Use try...except to catch and handle these exceptions gracefully
"""

main()