# Ask user how many people are in dinner group
group = input("Hello, how many people are in your dinner group? ")
group = int(group)

# if-else about amount of people for a table
if group > 8:
    print("Sorry, you will have to wait for a table")
else:
    print("Your table is ready!")