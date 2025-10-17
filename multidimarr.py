from numpy import *
arr1 = array ([[1,2,3],
            [4,5,6]
            ])
print(arr1.dtype)# it will give you the datatype of the array
print(arr1.ndim) # it will give you the number of dimension
print(arr1.shape) # it will give you the shape of the array , NUMBER OF ROWS AND COL
print(arr1.size)# it will give you the total number of elements in the array

#convert 2 d to 1 d array

arr2 =arr1.flatten() # it will convert 2 dim array to 1 d array

#metrix multiplication .use of metrix is in computer graphics , image processing , cryptography , 3d modelling
 m1 = matrix('1,2,3;4,5,6;7,8,9')
 m2 = matrix('1,2,3;4,5,6;7,8,9')
 m3 =m1+m2
print(m3)