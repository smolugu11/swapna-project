"""
List comprehension is a compact and elegant way to create a new list by transforming or filtering elements from an existing iterable (like a list, tuple, or range) — all in a single line of code.
new_list = [expression for item in iterable]

"""

def main():

    animals1 = ['cat', 'dog','cow','sheep']
    """
    animals2 = animals1 # 1 list but it assigned to both animals 1, 2
    del animals2[1]
    print(animals2)
    print(animals1)
    :return:
    """

# copy the list
#     animals3 = animals1.copy()
#     del animals3[1]
#     print(animals1)
#     print(animals3)

    animals4 = [animal.upper() for animal in animals1]
    """
    - Start with for animal in animals
- Python loops through each item in the animals list: 'cat', 'dog', 'cow'
- Apply animal.upper() to each item
- 'cat'.upper() → 'CAT'
- 'dog'.upper() → 'DOG'
- 'cow'.upper() → 'COW'
- Collect results into a new list
- Final result: ['CAT', 'DOG', 'COW']
    """
    print(animals4)

    numbers1 = [1,2,3,4,5]
    number2 = numbers1
    number2 = [x**2 for x in numbers1] #
    print(number2)
main()

# condition in list comperhensation
def condition():
    number3 = [x for x in range(0,10)]
    print(number3) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number4= [ x for x in number3 if x>5]
    print(number4) #[6, 7, 8, 9]
    number5 = [x for x in number3 if x%2 ==0]
    print(number5) #[0, 2, 4, 6, 8]

    numbers6 = [x for x in number3 if x % 2==1] # 1,3,5,7,9
    print(numbers6)

condition()