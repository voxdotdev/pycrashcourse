"""
Using your latest Restaurant class, store it in a module. 

Make a separate file that imports Restaurant. 

Make a restaurant instance, and call one of Restaurant's
methods to show that the import statement is working properly.

"""

from restaurant import Restaurant as Shop

fav_restaurant = Shop('Dim Sum Garden', 'Chinese')
fav_restaurant.describe_restaurant()
fav_restaurant.hours()