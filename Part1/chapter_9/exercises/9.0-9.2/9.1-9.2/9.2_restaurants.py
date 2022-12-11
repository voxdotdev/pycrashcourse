'''
Start with your class from 9-1. 

Create three different instances from the class 
Call describe_restaurant for each instance.

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

print("List of recommended restaurants:")
restaurant1 = Restaurant('Dim Sum Garden', 'Chinese')
print(f"{restaurant1.name} - {restaurant1.cuisine}")
restaurant2 = Restaurant('South Street Souvlaki', 'Greek')
print(f"{restaurant2.name} - {restaurant2.cuisine}")
restaurant3 = Restaurant('Alyans', 'Mediterranean')
print(f"{restaurant3.name} - {restaurant3.cuisine}")
