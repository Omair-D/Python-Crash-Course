class User:
    """Class for user profile"""
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
    
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

# Create different users and call both methods
user_1 = User('Kanye', 'West', 47, 'iforgor@gmail.com', 'Chicago')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Aubrey', 'Graham', 37, 'anitamaxwynn@hotmail.com', 'Toronto')
user_2.describe_user()
user_2.greet_user()