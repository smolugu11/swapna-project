def main():
    fruits = ['banana', 'apple', 'orange']

    print(len(fruits))
    print(fruits[1])
    print(fruits[0:2])

    test1 =list()#emapty list
    test2 = tuple() #empty tuple
    animals = ("fox", "cat","hen") #tuple
    for animals in animals:
        print(animals)
    print(animals)
    print(list(animals))  # converting tuple to list

# joing list together # lists
    fruits1 = ["apple", "banana", "orange"]
    fruits2 = ["watermelon", "kiwi", "starberry"]  #
    fruits1 += fruits2  # fruit1 is updated ['apple', 'banana', 'orange', 'watermelon', 'kiwi', 'starberry'] unline tuple
    print(fruits1)
    fruits1.extend(fruits2)  # it adds fruits 2 at the end
    value = 5
    # value + value+3
    value += 3
    print(value)
# obseve the diff between list and tuple
    animals1 = ('dog', 'cat', 'elephant')  # we cant change the tuple so
    animals2 = ('lion', 'cheta', 'pig')
    print(animals1)  # it created new tulpe  ('dog', 'cat', 'elephant', 'lion', 'cheta', 'pig')
    animals1 += animals2  # animal1 = animal1 +animals 2
    print(animals1)

# modfiying lists

    colors = ['red', 'green', 'blue']
    print(colors[1:2])  # - colors[1] → 'green' colors[2] → not included (slicing stops before this index)
    print(colors[
          :2])  # - colors[:2] slices the list from the beginning (index 0) up to but not including index 2. red-0, green -1
    print(colors[2:])  # colors[2:] slices the list starting from index 2 to the end. "blue"

    print(colors)
    colors.append("yellow") # add items to list and list can be modified
    print(colors)
#aacess items from the list
    print(colors[2])
    colors[2] = "purple" # you can change items in the list
    print(colors)
main()