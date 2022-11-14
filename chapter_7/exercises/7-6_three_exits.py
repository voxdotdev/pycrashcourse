'''
Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once: 

1) Use a conditional test in the while statement to stop the loop.
2) Use an active variable to control how long the loop runs. 
3) Use a break statement to exit the loop when the user enters a 'quit' value. 

Using exercise 7-4. 
'''

prompt = "\n 1. What toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' to finish) "

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"{topping.title()} will be added to your pizza!")

prompt = "\n2. What toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' to finish) "

max = 0

while True:
    topping = input(prompt)
    max += 1

    if max < 5:
        print(f"{topping} will be added to your pizza.")
    else:
        print(f"{topping} will be added to your pizza.")
        print(f"The maximum number of toppings, {max}, has been reached.")
        break

max = 0
while max < 5:
    topping = input("\n 3. What topping would you like on your pizza? ")
    max += 1
    if max < 5:
        print(f"{topping} has been added to your order!")
        continue
    
    print(f"\n The max amount of toppings, {max}, has been reached.")
    