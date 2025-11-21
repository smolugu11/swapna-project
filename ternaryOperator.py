"""
A ternary operator in Python is a shorthand way to write an if-else statement in a single line.
It chooses one of two values depending on whether a condition is True or False.
"""
# Syntax: value_if_true if condition else value_if_false

def main():
    value =7
    result ="Even" if value % 2 ==0 else "Odd"
    print(result)
    print("hello" if value==7 else "good bye")
main()