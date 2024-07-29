# Tests for equality and inequality with strings
language = 'English'
print(language == 'English')
print(language == 'Spanish')

print(language != 'French')
print(language != 'English')

# Tests using the lower() method
car = 'BMW'
print(car.lower() == 'bmw')
print(car.lower() == 'BMW')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
drinkingAge = 21
manAge = 20
womenAge = 23

print(manAge == drinkingAge)
print(womenAge == drinkingAge)

print(manAge > drinkingAge)
print(womenAge > drinkingAge)

print(manAge >= drinkingAge)
print(womenAge >= drinkingAge)

print(manAge <= drinkingAge)
print(womenAge <= drinkingAge)

# Tests using the and keyword and the or keyword
drinkingAge = 21
manAge = 20
womenAge = 23

print((manAge >= drinkingAge) and (womenAge >= drinkingAge))
print((manAge >= drinkingAge) or (womenAge >= drinkingAge))

# Test whether an item is in a list
foods = ['burger', 'fries', 'sushi', 'salmon', 'rice']

print('chicken' in foods)
print('burger' in foods)

# Test whether an item is not in a list
foods = ['burger', 'fries', 'sushi', 'salmon', 'rice']

print('fries' not in foods)
print('lasagna' not in foods)