
"""def is_even(n):
  return n % 2 == 0
even_nums = list(filter(is_even,nums))
insteaf of above 3 lines of code for fucntion we can use lambda function
even_nums = list(filter(lambda n: n%2 ==0,nums))"""

#FILTER : Filters elements in an iterable using a function .check how many even numbers are there in the list

nums = [3,2,46,7,7,8,9,4,2,1,5,6]
even_nums = list(filter(lambda n: n%2 ==0,nums)) # it will take the list from you and filter out even numbers. you need that filter as a list.
#filter take two arguments first is function name second is iterable(list, tuple, etc)
# 	Applies a function that returns True/False to every element
print(even_nums)

#MAP : Applies a function to every element in an iterable and returns a new iterable.
double = list(map(lambda n: n*2, nums)) # it will take the list from you and double each number. you need that map as a list.
print(double)

#Reduce : reduces an iterable to a single value by repeatedly applying a function. Import from functools.
from functools import reduce
# Example: Multiply all numbers together
numbs =[1,2,3,4]
product = reduce(lambda x, y: x * y, numbs)
print(product)

"""Function	Purpose	Example	Result
map	Transform each item	map(lambda x: x*2, [1,2,3])	
filter	Select items matching a rule	filter(lambda x: x>2, )	
reduce	Combine items cumulatively	reduce(lambda a,b: a+b,)"""