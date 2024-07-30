# Use dictionary to store info about 3 people
person_1 = {'age': 21, 'first_name': 'zack', 'last_name': 'cody', 'city': 'los angeles'}
person_2 = {'age': 25, 'first_name': 'blake', 'last_name': 'rodgers', 'city': 'new york'}
person_3 = {'age': 18, 'first_name': 'ryan', 'last_name': 'garcia', 'city': 'seattle'}

# Use a list to store the dictionaries
people = [person_1, person_2, person_3]

# Loop through list and print everything about each person
for person in people:
	name = f"{person['first_name'].title()} {person['last_name'].title()}"
	age = f"{person['age']}"
	location = f"{person['city'].title()}"

	print(f"{name}\n{age}\n{location}\n")