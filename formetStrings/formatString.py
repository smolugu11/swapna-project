def main():
    name = "Swapna"
    text ="Welcome to the world of Python."
    greeting= f"Hello {name}, {text}"
    print(greeting)
main()

#raw strings

def raw_string_example():
    dictory = r"C:\\new_folder\\temp"
    print(dictory)
raw_string_example()


class LunchBox:
    def __init__(self, main, fruit):
        self.main = main
        self.fruit = fruit
    def upma(self):
        print(f"Main dish is {self.main} and fruit is {self.fruit}")

box = LunchBox("Sandwich", "Apple")
box.upma()
LunchBox()