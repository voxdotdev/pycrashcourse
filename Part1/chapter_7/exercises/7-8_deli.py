'''
Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, 
such as 'i made your tuna sandwich'.

As each sandwich is moved, move it to the list of finished sandwiches. 

After all the sandwiches have been made, print a message listing 
each sandwich that was made.


'''

sandwich_orders = ['ham','swiss', 'turkey', 'pb&j']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I've made your {current_order}.")
    finished_sandwiches.append(current_order)

print("\nThe following orders have been completed")
for orders in finished_sandwiches:
    print(f"{orders.title()}")