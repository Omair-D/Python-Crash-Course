# Store pizzas in list
pizzas = ['pineapple pizza', 'cheese pizza', 'chicken pizza']

# Make copy of pizza list
friend_pizza = pizzas[:]

# Add a new pizza to the original list
pizzas.append('mushroom pizza')

# Add a different pizza to copy list
friend_pizza.append('buffalo pizza')

# Prove two seperate lists
print("My favorite pizzas are:")

# Use for-loop to print out first list
for pizza in pizzas:
	print(pizza)

# Now prove second list (copy)
print("My friend's favorite pizzas are: ")

# Using for-loop print the copy list
for pizza in friend_pizza:
	print(pizza)