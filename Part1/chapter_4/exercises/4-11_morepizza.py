# 4-11. My Pizza, Your Pizzas
## Start with the program from Exercise 4-1

pizzas = ['pepperoni', 'cheese', 'white']

## Make a copy of the list of pizzas, called friend_pizzas 
friend_pizza = pizzas[:]

## Add a new pizza to the original list
pizzas.append('blt')
## Add a different pizza to the list friend_pizzas
friend_pizza.append('bacon')
## Prove the lists are different by printing the message
## "My favorite pizzas are:" then use a for loop to print the second list

print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friend_pizza[:]:
    print(pizza.title())

## Make sure each pizza is stored in appropriate list.

# they are. 