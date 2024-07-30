# Empty list to store pets
pets = []

# Make a dictionary of different pets
pet_1 = {
	'type': 'dog',
	'color': 'brown',
	'owner': 'max',
	'favorite_food': 'treats',
}
pets.append(pet_1)

pet_2 = {
	'type': 'cat',
	'color': 'orange',
	'owner': 'bryan',
	'favorite_food': 'salmon',
}

pets.append(pet_2)

pet_3 = {
	'type': 'fish',
	'color': 'golden',
	'owner': 'drake',
	'favorite_food': 'fish food'
}

pets.append(pet_3)


# Loop throug list printing everything about each pet
for pet in pets:
	petType = f"Type: {pet['type'].title()}"
	petColor = f"Color: {pet['color'].title()}"
	petOwner = f"Owner: {pet['owner'].title()}"
	petFood = f"Favorite food: {pet['favorite_food'].title()}"

	print(f"{petType}\n{petColor}\n{petOwner}\n{petFood}\n")