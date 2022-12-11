"""
Responding to a Failed Test 

Examine the changes you just made to the function and figure out how those 
changes broke the desired behavior. 

In the folder Fail we required a middle name instead of optionally allowing one. 
We'll fix it here.

"""

def get_formatted_name(first, last, middle=''):
    """ Generate a neatly formatted full name. """
    if middle:
      full_name = f"{first} {middle} {last}"
    else: 
      full_name = f"{first} {last}"
    return full_name.title()