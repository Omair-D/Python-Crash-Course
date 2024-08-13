# Wrap code from addition.py into a while loop

print("Please enter 'q' to quit\n")

while True:
    try:
        first_number = input('Enter the first number: ')
        if first_number == 'q':
            break
        first_number = float(first_number)

        second_number = input('Enter the second number: ')
        if second_number == 'q':
            break
        second_number = float(second_number)

    except ValueError:
        print("Sorry, you can only add numerical values")
    else:
        print(f"Your sum is: {first_number + second_number}")

        
