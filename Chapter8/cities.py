# Define function describe_city() accepts two parameters city and country
def describe_city(city, country='United States'):
    print(f"\n{city.title()} is in {country.title()}")

# Call function for three different cities, at least one of which is not in the default country
describe_city('los angeles')
describe_city('akron')
describe_city('tokyo', 'japan')
