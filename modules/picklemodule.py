import  pickle

def main():
    numbers = [1.23,4,67,78,2]
    test = "Hello, nice weather today"
    lookup= { 1:'January', 2:'February', 3:'March'}

    with open("data.pkl", "wb") as file:
        pickle.dump(numbers, file)
        pickle.dump(test, file)
        pickle.dump(lookup, file)


    with open("data.pkl", "rb") as file:
        numbers = pickle.load(file)
        test = pickle.load(file)
        lookup = pickle.load(file)


    # with open("data.pkl", "rb") as file:
    #     numbers= pickle.load(file)
    #     test = pickle.load(file)
    #     lookup = pickle.load(file)
    #     print(test1)
    #     print(lookup)


    with open('data.pkl', 'rb') as file:
        while True:
            try:
                item = pickle.load(file)
                print(item)
            except EOFError:
                break

"""Every time through the loop, you read and print the next object stored in data.pkl.

When all objects are read, and you reach the end of the file, EOFError occurs, the exception is caught, and the loop breaks.

The code prints every pickled object inside the file, each on a new line."""
main()