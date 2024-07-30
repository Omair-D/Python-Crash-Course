# Make a list with five usernames
usernames = ['zack', 'brian', 'pikachu', 'charizard', 'admin']

# Write out greetings for each username and print a special greeting for 'admin'
for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {username.title()}, thank you for logging in again")
