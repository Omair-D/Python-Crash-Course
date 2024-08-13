# Import json
import json

# Prompt user for favorite number
favorite_number =  input("Enter your favorite number: ")

# Make a json file name
filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
