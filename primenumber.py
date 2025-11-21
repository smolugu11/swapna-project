#prime numbers are divisible by only 1 and itself

num =7
for i in range(2,num):
    if num % i == 0:
        print("not a prime number")
        break
else:
    print("prime number")



"""- num = 7: You're checking if 7 is a prime number.
- for i in range(2, num): Loops through numbers 2 to 6 (not including 7).
- if num % i == 0: Checks if 7 is divisible by any number in that range.
- If it is divisible, it’s not prime, and the loop breaks.
- else: (attached to the for loop, not the if):
- This else block runs only if the loop completes without hitting break.
- So if no divisors are found, it prints "prime number".
"""