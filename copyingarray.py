from numpy import *
arr = array([1,2,3,4,5]) #created an array
 # it will add 5 to each element in the array
print("additoin :", arr+5)

arr1 = array([1,2,3,4,5,6])
arr2 = array([7,8,9,10,11,12])
#Arithmetic operations on two arrays
arr3 = arr1 + arr2
print(arr3)
# print("Addition :",arr1+arr2)
print(sum(arr1)) # it will give you sum of all elements in the array
print(min(arr1)) # it will give you minimum element in the array
print(max(arr1)) # it will give you maximum element in the array
print("mean :",mean(arr1)) # summer of elemts / number of elements = 2.5.7. =14/3 =4.6
print("median :",median(arr1)) # it will give you median of all elements in the array
print("standard deviation :",std(arr1)) # it will give you standard deviation of all elements in the array
print("variance :",var(arr1)) # it will give you variance