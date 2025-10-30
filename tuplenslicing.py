"""
In Python, containers are data structures that hold and organize multiple elements — like lists, tuples, sets, and dictionaries. They’re essential for grouping, accessing, and manipulating data efficiently
tuples are immutable-cant be changed
list are mutable and can te changed
"""

def main():
    animals = ("dog", "cat","tiger", 'elephant','bird') # tuples are order, immutable( cant change)
    print(type(animals)) #type is a built in function that tells the data type
    number_animals = len(animals)
    print(number_animals)
    print(animals[1]) #accessing tuple elements by index
    for animal in animals:
        print(animal)

#slicing tuple
    print(animals[1:3]) # cat to ele all the way till 3 but not 3 as it starts from 0, 1, 2 ( are 3 )
    print(animals[2:]) # from tiger till end
    print(animals[-1]) # end of the list element is bird
    print(animals[-3:-1]) # - animals[-3] → "tiger" (3rd from the end,  animals[-1] → "bird" (but not included in slicing)

    text ="It was the best time"
    print(text)
    print(text[3])
    print(text[0:6])


main()
