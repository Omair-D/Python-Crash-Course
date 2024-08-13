# prompt user for numerical inputs to add
try:

    first_number = input('Enter the first number: ')
    first_number = float(first_number)

    second_number = input('Enter the second number: ')
    second_number = float(second_number)
except ValueError: # Catch error if they enter a non numerical value
    print("Sorry, you can only add numbers.")
else:
    print(f'The sum of your numbers is: {first_number + second_number}')