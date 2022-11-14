'''
Start with a copy of your program from Exercise 8-9.

Write a function called send_messages() that prints each text message 
and moves each message to a new list called sent_messages as it's printed. 

After calling the function, print both of your lists to make sure the messages were 
moved correctly. 
'''

def learning(unknown, known):
        """ Moving messages from one list to another. """
        while unknown:
            current_recipe = unknown.pop()
            print(f"You've just learned how to play {current_recipe}!")
            known.append(current_recipe)

def show_learned(known):
    """ Print each unknown recipe in the list """
    print(f"Learned recipes: {known}")

unknown = ['YKS', 'PLT', 'SWJ']
known = []

learning(unknown, known)
show_learned(known)

''' The code below this is printing the unknown recipes, if none, printing message saying so. 
'if not x' is saying 'if x is null/none'
This is redundant in this case, but in future more recipes would be added.
unknown would not be moved to known list until the function learning is called by another trigger, 
like user performing an action or confirming something that unlocks the recipe.'''

if not unknown:
    print("You've learned all the recipes!")
else: 
    for remaining in unknown:
        print(f"Remaining recipes: {remaining}")