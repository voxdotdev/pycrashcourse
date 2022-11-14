'''
Start with your work from Exercise 8-10. 
Call the function learning() with a copy of the list of recipes.

After calling the function, print both of your lists to show 
that the original list has retained its message.

This exercise is to demonstrate copying a list versus modifying it via slicing [:]. 

'''

# Functions

def learning(unknown, known):
    
    while unknown:
        current_recipe = unknown.pop()
        print(f"You've just learned the recipe {current_recipe}!")
        known.append(current_recipe)

def learned(known):
    if not known:
        print("You haven't learned any recipes..")
    else:
        print("Learned recipes:")
        for recipe in known:
            print(recipe)

def unlearned(unknown):
    if not unknown:
        print("Original list of recipes lost.")
    else: 
        print(f"Original list of recipes:")
        for recipe in unknown:
            print(recipe)

# Lists 

unknown = ['YKS', 'PLT', 'SWJ']
known = []

# Function calls

learning(unknown[:], known)
learned(known)
unlearned(unknown)

