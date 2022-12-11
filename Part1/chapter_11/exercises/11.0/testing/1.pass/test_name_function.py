""" 
A Passing Test 

The syntax for setting up a test case takes some getting used to, but once
you've set up the test case it's straightforward to add more unit tests for
your functions. 

To write a test case for a function, import the unittest module and the
function you want to test.

Then, create a class that inherits from unittest.TestCase, adn write a series
of methods to test different aspects of your function's behavior.

Here's a test case with one method that verifies that the function 
get_formatted_name() works correctly when given a first and last name:
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_Name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()



"""
After importing unittest and the function we want to test, we create a class
called NamesTestCase, which will contain a series of unit tests for get_formatted_name().

You can name the class anything you want, but it's best to call it something
related to the function you're about to test and to use the word Test in the class name.

The class must inherit from the class unittest.TestCase so Python knows how to run the
tests you write. 

NamesTestCase contains a single method called test_first_last_name().

Any method that starts with test_ will be run automatically when we run 
test_name_function.py. 

Within this method we call the function we want to test with the arguments, then assign
the result to formatted_name. 

We then use one of unittest's most useful features, an assert method.

Assert methods verify that a result you received matches the result you expected to receive.

Because we know get_formatted_name() is supposed to return a capitalized properly spaced
full name, we expect the value of formatted_name to be Janis Joplin. 

To check if this is true, we use unittest's assertEqual() method and pass formatted_name
and 'Janis Joplin'.

The line says 'Compare the value in formatted_name to the string 'Janis Joplin'. 
If they don't match, let me know! 

The if block at the bottom looks at a special variable __name__ which is set when the 
program is executed. If this file is being run as the main program, the value of
__name__ is set to '__main__'. 

In this case we call unittest.main(), which runs the test case. 

When a testing framework imports this file, the value of __name__ won't be '__main__'
and this block will not get executed. 

OUTPUT 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

The dot on the first line of the output tells us that a single test passed. 

The next line tells us that Python ran one test, and it took less than 0.001
seconds to run. 

The final OK tells us that all unit tests in the test case passed.

This output indicates that the function get_formatted_name() will always work
for names that have a first and last name, unless we modify the function. 

When we modify get_formatted_name(), we can run the test again. 
If the test case passes, we know the function still works for names like Janis Joplin.

"""