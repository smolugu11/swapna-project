numbers = ["zero", "one", "two", "three", "four", "five", "six","seven", "eight", "nine"]
print(numbers[2:5]) # It counts from 2 but not gonna add 5 as it counts from 0
print(numbers[3:9:2]) # starts at 3 which is three gap 2 , ['three', 'five', 'seven']
print(numbers[::])#prints all

greeting = "Hello there"
print(greeting[2]) # it will give you l index 2
print(greeting[::2]) # every other letter in the hello there

# inserting and extending with other lists

def main():
    animals = ['dog', 'cat', 'elephant']
    animals.insert(1, 'pig') #  it added pig infront of cat as cat index is 1
    print(animals)
    more_animals = ['tiger','fox']
    animals.extend(more_animals) # add more animals to animals
    print(animals)


#removing items from list
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    days[0:3] = [] #['Thu', 'Fri', 'Sat', 'Sun']
    print(days)
    days.remove("Sat")
    print(days)

    item = days.pop(0) # it removes thurs from days[0:3] = [] #['Thu', 'Fri', 'Sat', 'Sun']
    print(itemP8'NR')
    return




main()