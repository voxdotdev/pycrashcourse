'''
Start with your program from exercise 9-1

Add an attribute called number_served with a default value of 0.

Create an instance called restaurant from this class. 
- done previously 

Print the number of customers the restaurant has served, then
change this value and print it again. 

'''

class Restaurant:
    """ Restaurant details """

    def __init__(self, name, cuisine):
        " Initialize name and cuisine type attributes" 
        self.name = name 
        self.cuisine = cuisine
        self.number_served = 0
            
    def describe_restaurant(self):
        print(f"{self.name} is now open.")
        print(f"Number of people served: ") 

    def restaurant_info(self):
        print(f"{self.name} is open M-S 10:00 AM to 8:00 PM.")
        
        print(f"Number of people served: {self.number_served}")

restaurant = Restaurant('Dim Sum Garden', 'Chinese')

restaurant.restaurant_info()
restaurant.number_served = 5
restaurant.restaurant_info()

