"""
Toppings take two 

Make a list of toppings the customer has requested
Then, use a loop to announce each topping as it's added to the pizza. 

"""

toppings = ['cheese', 'bacon', 'pepperoni']

for toppings in toppings:
    print(f"Adding {toppings}.")

print("\nFinished making your pizza!\n")

"""
OUTPUT

Adding cheese.
Adding bacon.    
Adding pepperoni.

Finished making your pizza!

-----

But what if the pizzeria runs out of bacon? 
An if statement inside the for loop can handle this travesty appropriately. 
"""
topping = ['cheese', 'bacon', 'pepperoni']


for topping in topping:
    if topping == 'bacon':
        print("Sorry, we are out of bacon. :( ")
    else:
        print(f"Adding {topping}.")

print("\nFinished making your pizza!\n")

"""
OUTPUT

Adding cheese.
Sorry, we are out of bacon. :( 
Adding pepperoni.

Finished making your pizza!

"""

# Checking That a List is Not Empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\n Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

"""
OUTPUT

Are you sure you want a plain pizza?

As shown in the if statement, if the name of a list is used, Python returns True if the list 
contains at least one item. 

"""