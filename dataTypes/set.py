"""
list: ordered - Items stay in the order you added them

tuple :ordered
set: not ordered set uses curly brackets. Its not allow duplcate, mutable
"""

numbers ={ 1,1,2,3,4,5} # only dispaly 1 at once
print(numbers)

number_list = [1,2,3,4,5,6,6,7,7]
print(number_list) # gives [1, 2, 3, 4, 5, 6, 6, 7, 7]
print(set(number_list)) #gives {1, 2, 3, 4, 5, 6, 7} no duplicate

for number in numbers:
    print(number)
print( 3 in numbers)

"""Add and update sets"""

def main():
    numbers1 = {1,2,3}
    print(numbers1)
    numbers1.add(4)
    print(numbers1)
    numbers2 = {4,5,6,6,7}
    print(numbers2)
    numbers1.update(numbers2)
    print(numbers1)
    numbers1.update(["cat","dog"])
    print(numbers1)
main()


"""remove items from set"""
numbers = {x for x in range(15)}  # or for x in numbers: print(x)
print(numbers)
numbers.remove(1) # removes 1 which is index 2
print(numbers)

"""set union and intersection  """
def uni():
    num1 = {1,2,3}
    num2 = {4,5,6}
    print(num1.union(num2)) #
    print(num1)
    print(num1.intersection(num2))
    print(num1)
uni()

