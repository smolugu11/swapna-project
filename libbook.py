# 1. Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available= True # true if the book is available for borrowing
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")
    def return_book(self):
        if self.available:
            self.available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")
# 2. Create a collection of Book objects (the library)

library = [ Book("1984", "George Orwell"),
            Book("To Kill a Mockingbird", "Harper Lee"),
            Book("The Great Gatsby", "F. Scott Fitzgerald")]

# 3. Main loop,  Functions to display available books and manage borrowing/returning
while True:
    print("\nLibrary Menu:")
    print("1. View available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\nAvailable Books:")
        for idx, book in enumerate(library):
            if book.available:
                print(f"{idx + 1}. '{book.title}' by {book.author}")

    elif choice == '2':
        book_num = int(input("Enter the book number to borrow: ")) - 1
        if 0 <= book_num < len(library):
            library[book_num].borrow()
        else:
            print("Invalid book number.")

    elif choice == '3':
        book_num = int(input("Enter the book number to return: ")) - 1
        if 0 <= book_num < len(library):
            library[book_num].return_book()
        else:
            print("Invalid book number.")

    elif choice == '4':
        print("Exiting the library system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")