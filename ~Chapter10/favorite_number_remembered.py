import json

try:
    with open('numbers.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Enter your favorite number: ")
    with open('numbers.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print(f"Your favorite number is: {number}.")