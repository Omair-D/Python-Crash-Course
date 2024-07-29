# Store pizzas in list
pizzas = ['pineapple pizza', 'cheese pizza', 'chicken pizza']

# Use for loop to print each item in list
for pizza in pizzas:
	print(pizza.title())

# Modify loop to write a message along with the item

for pizza in pizzas:
	print(f"{pizza.title()} is so yummy!")
# Write message outside the for loop for my love of pizza
print("I love all of these pizzas so much!")