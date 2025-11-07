def main():
    file = open("ex.py", "a") # file= open(newfile.txt, 'w')
    file.write("hello, welcome to python file handling.")
    file.close()
    print("File written successfully.")
main()

def shoppingList():
    with open("shoppinglist.txt", "w") as file: # create a file and write items
        file.write("Milk\nEggs\nBread\nButter\n") # you can write like this also
         # end of the block it closes
    print("Shopping list created successfully.")

    with open("shoppinglist.txt", "r") as file: # you are again opening it to read
        content = file.read()
        print("Shopping List:")
        print(content)

    with open("shoppinglist.txt", "a") as file:
        file.write("this is new line added to the file.\n") # appending new item to the file
    print("Item added to the shopping list.")

shoppingList()