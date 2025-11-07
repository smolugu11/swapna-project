#single dimension array [1,2,3,4,5]
import array as arr
a = arr.array('i',[1,2,3,4,5])
print("Single dimension array")
for i in range (5):
    print(a[i])

from  numpy import *

arr =array([1,2,3,4,5,6],float) #single dimension array
print(arr.dtype)#data type of array
print(arr)

"""NumPy (short for Numerical Python) is a powerful open-source Python library used for scientific computing, especially when working with arrays, matrices, and numerical data.

🧠 What NumPy Does
- Provides the ndarray object — a fast, memory-efficient multi-dimensional array
- Supports vectorized operations (no need for Python loops)
- Includes tools for:
- Mathematical functions (e.g., sin, cos, log)
- Linear algebra (e.g., matrix multiplication, eigenvalues)
- Statistics (e.g., mean, median, standard deviation)
- Random number generation
- Fourier transforms
"""
arr = linspace(0,10,5) #linspace is a function in numpy i thas start, stop , end point
print(arr)
# it will create 5 values between 0 to 10 including both. Linear space is used to create an array of evenly spaced values over a specified range.
arr = arange(1,10,2) # it will create values between 1 to 10 but will skip 2 1,3,5,7,9,11,13
print(arr)

arr = logspace(1,40,5) # it will create 5 values between 10^1 to 10^40

arr = zeros(5) # it will create an array of 5 values with all values as 0 [0.0.0.0.0]
print(arr)