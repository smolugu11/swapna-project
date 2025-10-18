def fibnacci_sequence(n):
    a =0
    b=1
    print(a)
    print(b)

    for numbers in range(2,n):
        c= a + b
        a=b
        b=c
        print(c)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ( fib seq)
fibnacci_sequence(10)