favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Make list of people who polled and didn't
pollers = ['sarah', 'blake', 'phil', 'ryan', 'zack', 'edward', 'jen']

# Loop through list and print message if they need to take the poll using if-else statement
for people in pollers:
    if people in favorite_languages.keys():
        print(f"{people.title()}, thank you for taking the poll!\n")
    else:
        print(f"{people.title()}, please take the poll!\n")
