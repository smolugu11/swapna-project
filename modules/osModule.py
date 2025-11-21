"""
The os module in Python provides functions to interact with the operating system. It lets you:

Work with files and directories (create, remove, rename, list, etc.)

Access environment variables

Get current working directory or change it

Execute system commands

Interact with file paths

Query system information
"""

import os

def main():
    #print current working directory
    cwd = os.getcwd()
    print("Current Working Directory:", cwd)
    #list files and directories in current directory
    items = os.listdir(cwd)
    print("Files and Directories in '", cwd, "':", items)




main()