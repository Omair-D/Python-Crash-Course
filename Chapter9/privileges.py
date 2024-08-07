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

class Admin(User):
    """Illustrate admin user"""
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()

class Privileges():
    """Class to store a user with admin privileges"""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Show admin privileges"""
        print("\nUser privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f" = {privilege}")
        else:
            print("- This user has no privileges")

kanye = Admin('Kanye', 'West', 37, 'iforgor@gmail.com', 'Chicago')
kanye.describe_user()

print("\nAdding privileges...")
kanye_privileges = [
    'can ban users',
    'can add discussions',
    'can time out accounts',
]
kanye.privileges.privileges = kanye_privileges
kanye.privileges.show_privileges()
