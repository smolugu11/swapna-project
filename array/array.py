from array import * #imports the array module which has functions to create and manipulate arrays, classes and methods

arr = array('i', []) #create an empty array of integers

n =int(input("Enter the length of an array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x) #append adds the value to the end of the array
print(arr)

val = int(input("Enter the value to be searched: ")) #input value to be searched in the array

print(arr.index(val)) #index returns the index of the first occurrence of the specified value in the array
