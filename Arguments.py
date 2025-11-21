
def add(a,b): #formal arguments
    c = a+b #local variable as actual arguments
    print(c)

add(1,2) #possitional arguments if you metioned a=1 it will take 1 as a and 2 as b theey called keword arguments
#add(b=2,a=1) #keyword arguments
#add(1,b=2) #mixed arguments
# variable length arguments make sure your funct can accept multi args

def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)

# b =(3,4,5) or
sum(3,4,5) #unpacking arguments now be takes all these 3 balues, it can take any number of arguments