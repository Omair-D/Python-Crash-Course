class Restaurant:
    """Simple attempt to replicate restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Method describing restuarant"""
        print(f"\nThe restaurant is: {self.restaurant_name}")
        print(f"The cuisine type is: {self.cuisine_type}")
        print(f"The number served is: {self.number_served}")
    
    def open_restaurant(self):
        """Method simulating restaurant open"""
        print(f"\n{self.restaurant_name} is now open!")
    
    def set_number_served(self, number):
        """A simple method to set number served"""
        self.number_served = number

    def increment_number_served(self, served):
        """A simple attempt at incrementing number served"""
        self.number_served += served

# Printing value of number served
restaurant = Restaurant('Red Lobster', 'Seafood')
restaurant.describe_restaurant()

# Change value of number served and print again
restaurant.number_served = 50
restaurant.describe_restaurant()

# Use new set_number_served() to change value
restaurant.set_number_served(89)
restaurant.describe_restaurant()

# Use increment_number_served() to increase the amount served
restaurant.increment_number_served(11)
restaurant.describe_restaurant()