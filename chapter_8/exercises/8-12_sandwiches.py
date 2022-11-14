'''
Write a function that accepts a list of items a person wants on a sandwich. 

The function should have one parameter that collects as many items as 
the function call provides, and it should print a summary of the sandwich 
that's being ordered. 

Call the function three times, using a different number of arguments each time. 

'''

def sandwich_toppings(*toppings):
    print("Sandwich order:")
    for topping in toppings:
        print(topping.title())

sandwich_toppings('turkey', 'swiss', 'lettuce', 'tomato')
sandwich_toppings('ham', 'provolone', 'mustard', 'lettuce','tomato')
sandwich_toppings('egg', 'cheese', 'bacon')