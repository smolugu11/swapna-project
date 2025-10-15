def list():
    #list is mutable(can be changed) and ordered collection of items
    num = [1,2,4,5,6,5]
    print(num[0]) #print first number in the list
    print(num[2:]) #print in between the list from 3rd number to end
    print(num[-1]) #which print last number in the list
    # names = ["john", "doe", "smith"]
    # list =["sapna",1,1.1 ] #list can have diffrent type of data
    num.insert(0,5) # you are interting 5 at index 0
    num.append(7)  #Adds item 7 to the end of the list
    num.pop(0) #removes item at index 0
    num.count(5) #Returns the number of times x appears
    num.sort()#Sorts the items of the list in place
    num.reverse() #Reverses the elements of the list in place

list()