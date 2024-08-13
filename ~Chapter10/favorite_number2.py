import json

def get_number():
    filename = 'numbers.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        print(f"Your favorite number is: {number}")
        return number
    
get_number()