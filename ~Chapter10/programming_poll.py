fileName = 'poll.txt'

# Use while loop to keep polling
print("\nPlease enter 'quit' to end program.")

while True:
    pollAnswer = input("Why do you like programming? ")

    if pollAnswer == 'quit':
        break
    else:
        with open(fileName, 'a') as f:
            f.write(f"{pollAnswer}\n")

