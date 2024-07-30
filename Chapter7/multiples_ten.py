# Ask user for a number
userNum = input("Give me any number: ")
userNum = int(userNum)

# Check if the number is a multiple of 10
if userNum % 10 == 0:
    print("Your number is a multiple of 10!")
else:
    print("Your number is not a multiple of 10.")