#Recursion : where a function calls itself. The function calls itself with a smaller number each time (n-1).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #  Recursive call

    """
    for loop
    def factorial(n):
        result = 1
        for n in range(1, n + 1): # - range(1, 6) → generates: 1, 2, 3, 4, 5

            result = result * i
            "- result = 1
- result = 1 * 1 = 1
- result = 1 * 2 = 2
- result = 2 * 3 = 6
- result = 6 * 4 = 24
- result = 24 * 5 = 120
✅ Final result: 120


        return result
    print(factorial(5)) 
    
    """
print(factorial(5))

"""
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1
Final result: 5*4*3*2*1 = 120

Once n reaches 0 or 1, it returns 1 and the recursion unwinds, multiplying all previous n values together.
"""