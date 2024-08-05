class Restaurant:
    """Simple attempt to replicate restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Method describing restuarant"""
        print(f"\nThe restaurant is: {self.restaurant_name}")
        print(f"The cuisine type is: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Method simulating restaurant open"""
        print(f"\n{self.restaurant_name} is now open!")

# Printing both attributes of class
restaurant = Restaurant('Red Lobster', 'Seafood')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling both methods in the class
restaurant.describe_restaurant()
restaurant.open_restaurant()