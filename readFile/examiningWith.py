class LogFile:
    def __init__(self,filename):
        self.filename = filename
        self.file = None # Initialize file attribute
    def __enter__(self):
        self.file = open(self.filename, "a") # Open file in append mode
        print(f"Log file {self.filename} opened.")
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print(f"Log file {self.filename} closed.")

        if exc_type:
            print(f"An exception occurred: {exc_value}")
        # Handle exceptions if necessary

with LogFile("break.py") as log:
    log.write("This is a log entry.\n")
    log.write("Logging another entry.\n")
    print("Log entires written.")


"""
What exactly do they do?
with: Ensures reliable setup and cleanup, so you don’t forget to close or release resources.

__enter__: Handles the resource acquisition or setup.

__exit__: Handles cleanup, even if the block code throws an error.

They make your Python code cleaner, safer, and more reliable—especially for files, hardware, databases, or anything that you open and must always close.

Let me know if you want a visual diagram, a practical example for hardware, or see what happens if you don’t use them!

When the block ends (even if there’s an error), __exit__ automatically closes the file and can log any exceptions.
The with Statement
The with statement is used to wrap the execution of a block with methods defined by a context manager (a class with __enter__ and __exit__).

Its main purpose is to automatically manage resources—like opening and closing files, acquiring and releasing locks, establishing and terminating connections.

__enter__ Method
This method is called at the start of the with block.

Its job: set up what you need (open files, connect to database, etc.).

It can return a resource to be used inside the with block (e.g., the file object).

__exit__ Method
This method is called automatically at the end of the with block—no matter what happens inside (success OR error).

Its job: clean up resources (close files, release locks, disconnect).

It receives info about exceptions, so you can handle errors gracefully.

"""