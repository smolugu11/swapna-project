import re # This gives you access to regular expression functions in Python.

# match 0 or more matches of the preceding element
def main():
    text='drooool'

    restuls= re.match('dro*l', text)
    if restuls:
        print(restuls.group())
    else:
        print("No match found")
main()



"""
The main purpose of regular expressions (RegEx) in Python is to search fo]GH\TAAAAAAAAAAAYYYYYYYYRAAr, match, extract, and manipulate specific patterns of text within strings using the re module.​

Regular expressions work like a pattern-matching language. They allow you to define rules describing what text structures you want to find—such as words, numbers, emails, or specific formats (like dates or phone numbers).​

For example, RegEx can:

Check if a string matches a pattern (like verifying an email)

Search for a substring that fits a pattern

Extract parts of text (like numbers from a document)

Replace parts of a string with something else.​

How It’s Used in Python
Python provides these core functions in the re module:

re.search() — looks for a pattern anywhere in a string

re.match() — checks if the start of a string matches

re.findall() — finds all occurrences of a pattern

re.sub() — replaces matching parts of text

re.split() — splits a string by a pattern."""