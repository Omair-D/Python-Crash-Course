# Dictionary of people and favorite places
favPlaces = {
	'drake': ['toronto', 'california'],
	'lil wayne': ['atlanta', 'california', 'japan'],
	'kai cenat': ['new york', 'atlanta']
}

# Loop through stating name and favorite places

for person, location in favPlaces.items():
	print(f"{person.title()}'s favorite places are:")

	for place in location:
		print(f"\t{place.title()}\n")
