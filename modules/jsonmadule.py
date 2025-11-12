#JSON
import json

def main():
    numbers = [1.23,4,67,78,2]
    text = "Hello, nice weather today"
    with open("data1.json", "w") as file:
        json.dump(numbers, file)
        json.dump(text, file)

    with open('data1.json', 'r') as file:
        for line in file:
            try:
                obj = json.load(line)
                print(obj)
            except json.JSONDecodeError:
                print("Error decoding JSON line")
main()