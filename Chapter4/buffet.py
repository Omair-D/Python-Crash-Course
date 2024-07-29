# Five foods stored in a tuple
foods = ('burger', 'fries', 'sushi', 'salmon', 'rice')

# Use a for-loop to print out each food the restaurant offers
for menu in foods:
	print(menu)

# Try to modify one of the items and make sure Python rejects the change
# This will be rejected v
# foods.append('chicken')

# Add a line to rewrite tuple, add two foods
foods = foods = ('burger', 'chicken', 'sushi', 'caviar', 'rice')

# Print the revised menu with for-loop
for menu in foods:
	print(menu)