'''
Write a loop that prompts the user to enter a series of pizza toppings until they 
enter a 'quit' value. As they enter each topping, print a message saying 
you'll add that topping to their pizza. 

'''


prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' to finish) "

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"{topping.title()} will be added to your pizza!")