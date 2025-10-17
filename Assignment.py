# Write a Python program to print all names from a list that are less than or equal to 5 characters long. If a name is longer than 5 characters, print "name is too long".

def name():
    name_list = ['sapna', 'anurag', 'rahul', 'deepak', 'sonu', 'aman', 'ajay', 'vikas','ayra''aadhya']
    for name in name_list:
        if len(name) <= 5:
            print(name)
        else:
            print("name is too long")

name()

#give list print even and odd

def even_odd():

    even =0 # it adds events numbers count  # use f8 to debug
    odd =0
    for numbers in lst :
        if numbers % 2 == 0:
            even +=1
        else:
            odd +=1
    print("event numbers are :", even)
    print("odd numbers are :", odd)
lst = [10,12,13,15,16,17,13,18,20,21,22]
even_odd()
