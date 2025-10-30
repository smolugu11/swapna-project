def main():
    elements = (True, 3.2, 5, "cat") #packing
    (is_raining, weight, volume, animal) = elements #unpack
    print(is_raining)
    print(weight)
    print(volume)
    print(animal)

    fruits= ('banana','apple','pear','mango','kiwi')
    (fruit1,fruit2,fruit3, *more_fruits) = fruits
    print(fruit1)
    print(fruit2)
    print(fruit3)
    print(type(fruits))
    print(*more_fruits)

main()

