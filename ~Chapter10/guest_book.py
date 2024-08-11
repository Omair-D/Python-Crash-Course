# Write while loop to prompt user for name
# Print them a greeting and add line to file should be \n

fileName = 'guest_book.txt'

print('Please enter quit when finished\n')

while True:
    name = input("What is your name? ")

    if name == 'quit':
        break
    else:
        with open(fileName, 'a') as f:
            f.write(f"{name}\n")
    
    print(f"Hi {name}, welcome!")