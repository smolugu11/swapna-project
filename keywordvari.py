#if you wanna pass arguments with keywords use **variable name in fucntion definition

def person(name, **data):
    print(name)
    for key, value in data.items(): #or for key i, j in data.items():
        print(f"{key} : {value}")

person("Aadhya" , age = 8,city="ottawa", mobile=123456)