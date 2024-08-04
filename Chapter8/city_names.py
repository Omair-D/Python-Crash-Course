# Write function city_country() that takes two parameters
def city_country(city, country):
    format_location = f"\n{city.title()}, {country.title()}"
    return format_location

# Call function three times
city1 = city_country('los angeles', 'united states')
print(city1)

city2 = city_country('seattle', 'united states')
print(city2)

city3 = city_country('tokyo', 'japan')
print(city3)