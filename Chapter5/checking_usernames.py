# Program that ensures everyone has a unique username

# Make a list of five usernames
current_users = ['pikachu', 'charizard', 'max', 'jinx', 'yone']

# Make another list of new usernames
new_users = ['YOne', 'sora', 'Charizard', 'cloud', 'riku']

# Case sensitive check list
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users to see if each username has been used
for new_user in new_users:
    if new_user.lower() in current_users_lower:
	    print(f"Sorry {new_user} is taken! Choose a different username")
    else:
    	print(f"{new_user} is available!")