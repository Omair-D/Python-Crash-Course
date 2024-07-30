# Make dictionary of 3 rivers and country
rivers = {
	'nile river': 'egypt',
	'amazon river': 'ecuador',
	'yangtze river': 'china'
}

# Use a loop to print sentence of each river
for river, location in rivers.items():
	print(f"The {river.title()} runs through {location.title()}\n")

# Use a loop to print name of each river in dictionary
for river in rivers.keys():
	print(f"{river.title()}\n")

# Use a loop to print name of each location
for location in rivers.values():
	print(f"{location.title()}\n")