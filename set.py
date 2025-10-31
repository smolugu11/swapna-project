"""
list: ordered - Items stay in the order you added them

tuple :ordered
set: not ordered set uses curly brackets. Its not allow duplcate
"""

numbers ={ 1,1,2,3,4,5} # only dispaly 1 at once
print(numbers)

number_list = [1,2,3,4,5,6,6,7,7]
print(number_list) # gives [1, 2, 3, 4, 5, 6, 6, 7, 7]
print(set(number_list)) #gives {1, 2, 3, 4, 5, 6, 7} no duplicate

for number in numbers:
    print(number)
print( 3 in numbers)