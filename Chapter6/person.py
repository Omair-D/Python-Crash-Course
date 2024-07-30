# Use dictionary to store info about a person
person = {'age': 21, 'first_name': 'zack', 'last_name': 'cody', 'city': 'los angeles'}

first_name = person['first_name']
last_name = person['last_name']
age = person['age']
city = person['city']


# Print each piece of information stored in dictionairy
print(f"First name: {first_name.title()}")
print(f"Last name: {last_name.title()}")
print(f"Age: {age}")
print(f"City: {city.title()}")