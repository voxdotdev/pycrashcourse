'''
Storing Your Functions in Modules 

You can go a step further above using descriptive names for your functions
by storing your functions in a separate file called a module and then importing 
that module into your main program. 

An import statement tells Python to make the code in a module available in the currently 
running program file. 

Storing your functions in  a separate file allows you to hide the details of your
program's code and focus on its higher-level logic. When you store your functions in 
separate files, you can share those files with other programmers without having to share
your entire program. Knowing how to import also allows you to use libraries of functions 
that other programmers have written. 

There are several ways to import a module. 


Importing an Entire Module 

To start importing functions, we first need to create a module. A module is a file 
ending in .py that contains the code you want to import into your program. 
Let's make a module that contains the function make_pizza(). To make this module, we'll
remove everything from the file pizza.py except the function make_pizza():

'''

def make_pizza(size, *toppings):
    """ Summarize the pizza we are about to make. """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

'''
Now we'll make a separate file called making_pizzas.py in the same directory as pizza.py.
This file imports the module we just created and then makes two calls to make_pizza().

'''