# Store a list of numbers 1 - 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through list and use if-elif-else chain to put proper ending on ordinal numbers
for number in numbers:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")