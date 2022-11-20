'''
Make a class called Restaurant. 

The __init__ method() for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type. 

Make a method called describe_restaurant() that prints a message indicating that
the restaurant is open. 

Make an instance called restaurant from your class. 

Print the two attributes individually, then call both methods. 

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

restaurant = Restaurant('Dim Sum Garden', 'Chinese')

print(f"My favorite restaurant is {restaurant.name}.")
print(f"They serve {restaurant.cuisine} food.")

restaurant.describe_restaurant()
restaurant.hours()


