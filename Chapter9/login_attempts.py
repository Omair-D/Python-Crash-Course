class User:
    """Class for user profile"""
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        """Increment login attempt by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0

    def describe_user(self):
        """Giving summary of user profile"""
        fullName = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nName: {fullName}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Method to give greeting to user"""
        print(f"\nWelcome {self.first_name.title()}, check out the news in {self.location}!")

# Create instance and start incrementing the login attempt
user_1 = User('Kanye', 'West', 47, 'iforgor@gmail.com', 'Chicago')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# Print login attempts
print(f"{user_1.login_attempts}")

# Reset the login attempts to zero and print again
user_1.reset_login_attempts()
print(f"{user_1.login_attempts}")