"""
# Print Even Numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)
"""

for i in range (2,21,1):
    if i % 2 ==0:
        print("Even numbers :", i)
    else:
        print("Not an even number")

"""
Loop Through a List of Ingredients
ingredients = ["rice", "carrot", "egg", "soy sauce"]
"""
items = ["rice", "carrot", "egg", "soy sauce"]
for item in items:
    print(items)
"""
Countdown from 10 to 1
"""
for i in range(10,1,-1):
    print(i)

"""print mutlplication table"""

for i in range(1,11):
    print(f"5X{i} = {5*i}")
#while
"""Print Numbers Until 10"""
i =10
while i <=0:
    print(i)
    i += 10
"""Ask for Input Until Correct Answer"""

answer = ""
while answer != "yes":
    answer = input("Enter Answer: ")

ratings = []
while True:
    entry = input("Enter rating or 'done': ")
    if entry == "done":
        break
    ratings.append(int(entry))
print("All ratings:", ratings)

