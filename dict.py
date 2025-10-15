def data():
    try:
        people = {1:"Sapna", 2:"Kiran",4:"Ayra"} #key and value pair
        print(people[2]) # fecthes value of key 2
        people.get(3)
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