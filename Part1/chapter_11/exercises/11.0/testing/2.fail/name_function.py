"""
A Failing Test

Let's modify get_formatted_name() so it can handle middle names, 
but we'll do so in a way that breaks the function for names
with just a first and last name, like Janis Jopin. 

"""

def get_formatted_name(first, middle ,last):
    """ Generate a neatly formatted full name. """
    full_name = f"{first} {middle} {last}"
    return full_name.title()


"""
This time, running the file test_name_function.py returns this output:

E
======================================================================
ERROR: test_first_last_Name (__main__.NamesTestCase)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "d:\2022REPOS\PyCrashCourse\chapter_11\exercises\11.0\testing\fail\test_name_function.py", line 26, in test_first_last_Name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)


* The first item, E, tells us one unit test in the test case resulted in an error. 
Next we see that test_first_last_Name caused the error. 
"""