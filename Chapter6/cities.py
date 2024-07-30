# Create nested dictionary about cities
cities = {
	'los angeles': {
		'population': 3795936,
		'country': 'united states of america',
		'fun_fact': 'Los Angeles Was the First City to Measure the Speed of Light',
	},

	'new york': {
		'population': 8258035,
		'country': 'united states of america',
		'fun_fact': 'Pizza is a huge deal.',
	},

	'tokyo': {
		'population': 37115035,
		'country': 'japan',
		'fun_fact': 'Tokyo has more Michelin-starred restaurants than any other city in the world.'
	}
}

# Print name of each city and everything about them
for city, city_stats in cities.items():
	cityPop = city_stats['population']
	cityCountry = city_stats['country']
	cityFact = city_stats['fun_fact']

	print(f"{city.title()}:")
	print(f"Has a approx. population of: {cityPop}")
	print(f"Located in {cityCountry.title()}")
	print(f"fun fact: {cityFact}\n")