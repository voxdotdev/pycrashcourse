"""
Testing a function

To learn about testing, we need code to test.
Here's a simple function that takes in a first and last name, then
returns a neatly formatted full name:
"""

def get_formatted_name(first, last):
    """ Generate a neatly formatted full name. """
    full_name = f"{first} {last}"
    return full_name.title()

"""
The function above combines the first and last name with a space in between
to complete a full name, and then capitalizes and returns the full name. 

To check that get_formatted_name() works, let's make a program that uses 
this function. The program names.py lets users enter a first and last
name, then the program returns a neatly formatted full name. 
"""