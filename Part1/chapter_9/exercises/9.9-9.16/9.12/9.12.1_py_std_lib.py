"""
The Python Standard Library 
https://docs.python.org/3/library/

The Python standard library is a set of modules included with every Python installation. 

Now that you have a basic understanding of how functions and classes work, 
you can start to use modules like these that other programmers have written. 

You can use any function or class in the standard library by including a simple import
statement at the top of your file. 

For example, the module 'random' which can be useful in modeling many real-world situations.

One function from the random module is randint().

This function takes two integer arguments and returns a randomly selected integer 
between (and including) those numbers. 

"""

from random import randint
print(randint(1, 6))

"""
Another useful function is choice().

This function takes in a list of tuple and returns a randomly chosen element: 
"""

from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

first_up = choice(players)
print(first_up)

"""
You can also download modules from external sources. You'll see a number of these examples
in Part II, where we'll need external modules to complete each project.
"""