#dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Dictionaries are written with curly brackets, and have keys and values.
# Example: {"name": "John", "age": 30, "city": "

def data():
    try:
        people = {1:"Sapna", 2:"Kiran",4:"Ayra"} #key and value pair
        print(people[2]) # fecthes value of key 2
        people.get(3) #return none as there is no value for key 3
        people[3] = "Aadhya" #adding new key and value pair
        print(people)
        dect1 = ['Ayra', 'Aadhya', 'Danika']
        dect2 = ['python', 'java', 'net']

        # Combine both lists into a dictionary
        combined = dict(zip(dect1, dect2))
        print("Combined dictionary:", combined)
        print(combined['Ayra']) #fetch value of key 'Ayra'
    except Exception as e:
        print("error is ", e)
data()

# add two dict
prog = {'Js':'React', 'Python':['pycharm','sublime'] ,'java':{'jse','jme'}} #in the dict you have list and another dictry. we can fetch values

person = {
    'name': 'Swapna',
    'role': 'QA Engineer',
    'location': 'Ottawa'
}

print(person.get('name'))         # Swapna
print(person.keys())              # dict_keys(['name', 'role', 'location'])
print(person.items())             # dict_items([('name', 'Swapna'), ('role', 'QA Engineer'), ('location', 'Ottawa')])

# get(key[,default])	Returns the value of the specified key. If the key does not exist, return default (None if not provided)
# keys()	Returns a view object that displays a list of all the keys in the dictionary
# items()	Returns a view object that displays a list of a dictionary's key-value tuples
# values()	Returns a view object that displays a list of all the values in the dictionary
# pop(key[,default])	Removes the item with the specified key and returns its value. If the key does not exist, return default (raises KeyError if not provided)
# popitem()	Removes and returns the last inserted key-value pair as a tuple. Raises KeyError if the dictionary is empty
# update([other])	Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs
# clear()	Removes all items from the dictionary
# copy()	Returns a shallow copy of the dictionary
# fromkeys(iterable[,value])	Returns a new dictionary with keys from iterable and values
# setdefault(key[,default])	Returns the value of the specified key. If the key does not exist, insert the key with the specified default value (None if not provided)