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
        self.privileges = []
    
    def show_privileges(self):
        """Show admin privileges"""
        print(f"\n{self.first_name} has the following privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

kanye = Admin('Kanye', 'West', 37, 'iforgor@gmail.com', 'Chicago')
kanye.privileges = ['Can delete post', 'Can ban user', 'Can add post', 'Can time out user', 'Can kick user']

kanye.describe_user()
kanye.show_privileges()