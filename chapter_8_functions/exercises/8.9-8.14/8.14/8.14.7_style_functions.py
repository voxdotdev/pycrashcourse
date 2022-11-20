'''
Styling Functions

A few details need to kept in mind when styling functions. 

# Functions should have descriptive names. These names should use lowercase letters and underscores. Descriptive names help you and others
understand what your code is trying to do. Module names should use these 
conventions as well. 

# Every function should have a comment that explains concisely what 
the function does. This comment should appear immediately after the 
function definition and use the docstring format. 

If you specify a default value for a parameter, no spaces should be used 
on either side of the equal sign: 

del function_name(parameter_0, parameter_1='default value')

The same convention should be used for keyword arguments in function calls: 

function_name(value_0, parameter_1='value')

# PEP 8 https://www.python.org/dev/peps/pep-0008/ recommends that you limit lines
of code to 79 characters so every line is visible in a reasonable sized editor window. 
If a set of parameters causes a function's definition to be longer than 79 characters, 
press ENTER after the opening parenthesis on the definition line.

On the next line, press TAB twice to separate the list of arguments from the body of the function, 
which will only be indented one level. 
Most editors automatically line up any additional lines of parameters to match the indentation 
you have established on the first line: 

def function name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...

If your program or module has more than one function, you can separate each by two blank 
lines to make it easier to see where one function ends and the next one begins. 

All import statements should be written at the beginning of a file. 
The only exception is if you use comments at the beginning of your file to describe the overall program.

'''

