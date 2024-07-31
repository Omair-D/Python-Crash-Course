# Empty dictionary
vacation = {}

# Poll user about name and dream vacation
pollActive = True

while pollActive:
    # Variables for name and response
    name = input("\nEnter your name: ")
    response = input("What is your dream vacation: ")

    # Record response in dictionary
    vacation[name] = response
    
    # Continue and ask if anyone else will take poll
    contPoll = input("Would another person take a poll? ('yes'/'no') ")

    if contPoll == 'no':
        pollActive = False

# Show poll results
print("\n===Poll Results===")

for name, response in vacation.items():
    print(f"{name.title()}'s dream vacation is {response}.")