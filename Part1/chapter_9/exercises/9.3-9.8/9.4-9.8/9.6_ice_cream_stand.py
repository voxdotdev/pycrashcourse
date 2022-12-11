'''
An ice cream stand is a specific kind of restaurant. 

Write a class called IceCreamStand that inherits from the Restaurant class 
written in exercise 9-1 or 9-4. 

Either version of the class will work; just pick the one you like better. 

Add an attribute called flavors that stores a list of ice cream flavors. 

Write a method that displays these flavors. 

Create an instance of IceCreamStand and call this method.

'''

class Restaurant:
    """ Restaurant details """

    def __init__(self, name, cuisine):
        " Initialize name and cuisine type attributes "
        self.name = name 
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"{self.name} is now open.")

    def hours(self):
        print(f"{self.name} is open M-S 10:00 AM to 8:00 PM.")

class IceCreamStand(Restaurant):
    """ Initialization of the icecream stand."""
    
    def __init__(self, name, cuisine,):
        super().__init__(name, cuisine)

        self.flavors = ['chocolate','vanilla','strawberry']

    def display_flavors(self):
        """ Display available ice cream flavors. """

        print(f"The {self.name.title()} shop has the following ice cream flavors:")
        for flavor in self.flavors:
            print(flavor.title())

ice_cream = IceCreamStand('I scream!', 'Dessert')

ice_cream.display_flavors()