'''
Using the sandwich orders from 7-8, make sure the sandwich 'pastrami'
appears in the list at least three times. Add code near the beginning of your
program to print a message saying the deli has run out of pastrami.

Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 

Make sure no pastrami sandwiches end up in finished. 

'''

sandwich_orders = ['ham', 'pastrami', 'swiss', 'pastrami', 'turkey', 'pastrami', 'pb&j']

finished_sandwiches = []

print("\nNow working on orders, please be advised we are out of pastrami.\n")

while sandwich_orders:

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    current_order = sandwich_orders.pop()

    print(f"I've made your {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following orders have been completed")
for orders in finished_sandwiches:
    print(f"{orders.title()}")