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

class IceCreamStand(Restaurant):
    """Simple attempts at representing an ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display ice cream flavors"""
        print(f"\nThe following flavors are available: ")
        for flavor in self.flavors:
            print(f"-{flavor}")
ice_cream_1 = IceCreamStand("Handel's")
ice_cream_1.flavors = ['Blue Moon', 'Vanilla', 'Chocolate', 'Strawberry', 'Mint']

ice_cream_1.describe_restaurant()
ice_cream_1.show_flavors()