'''
Modifying a List in a Function 

When you pass a list to a function, the function can modify the list.
Any changes made to the list inside the function's body are permanent, 
allowing you to work efficiently even when you're dealing with large 
amounts of data. 

Consider a company that creates 3D printed models of designs that users 
submit. Designs that need to be printed are stored in a list, and after 
being printed they're moved to a separate list. The following code does this 
without using functions: 

'''

# Start with some designs that need to be printed. 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left. 
# Move each design to completed_models after printing. 

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models. 
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

'''
We can reorganize this code by writing two functions, each of which does one specific job. 
Most of the code won't change; we're just making it more carefully structured. 

The first function will handle printing the designs, and the second will summarize the 
prints that have been made: 

'''

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left. 
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ Show all the models that were printed. """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

'''
This program is easier to extend and maintain than the version without functions.
If we need to print more designs later on, we can simply call print_models()
again. If we realize the printing code needs to be modified, we can change the code 
once, and our changes will take place everywhere the function is called. 

This example also demonstrates that every function should have one specific job. 
The first function prints each design, and the second displays the completed models.
This is more beneficial than using one function to do both jobs. 

If you're writing a function and notice the function is doing too many different tasks, 
try to split the code into two functions. 

Remember that you can always call a function from another function, which can be 
helpful when splitting up a complex task into a series of steps. 

'''

''' 
Preventing a function from Modifying a List 

Say yo start with a list of unprinted designs and write a function to move them 
to a list of completed models, as in the previous example. 

You may decide that even though you've printed all the designs, you want to keep 
the original list of unprinted designs for your records. 

However, because you moved all the design names out of unprinted_designs, the list is
now empty, and the empty list is the only version you have; the original is gone. 

In this case, you can address this issue by passing the function a copy of the list, 
not the original. Any changes the function makes to the list will affect only the copy.

'''

# function_name(list_name[:])

'''
The slice notation [:] makes a copy of the list to send to the function. 
If we didn't want to empty the list of unprinted designs in print_models.py, we 
could call print_models() like this:

'''

print_models(unprinted_designs[:], completed_models)

'''
Even though you can preserve the contents of a list by passing a copy of it 
to your functions, you should pass the original list to functions unless you have
a specific reason to pass a copy. It's more efficient for a function to work with 
an existing list to avoid using the time and memory needed to make a separate copy, 
especially when working with large lists. 

'''