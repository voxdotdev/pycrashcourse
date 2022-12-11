"""
Python uses special objects called exceptions to manage errors that 
arise during a program's execution. Whenever an error occurs that makes Python
unsure what to do next, it creates an exception object. 

If you write code that handles the exception, the program will continue running. 
If you don't handle the exception, the program will halt and show a traceback, 
which includes a report of the exception that was raised. 

Exceptions are handled with try-except blocks. A try-except block asks Python 
to do something, but it also tells Python what to do if an exception is raised. 

When you use try-except blocks, your programs will continue running even if things
start to go wrong. Instead of tracebacks, which can be confusing for users to read, 
users will see friendly error messages that you write. 

Handling the ZeroDivisionError Exception 

Division by zero is impossible, so obviously Python can't do it. 
Let's ask it to anyway. 
"""

# print(5/0)

"""
OUTPUT
Traceback (most recent call last):
  File "d:\2022REPOS\.....\division_calc.py", line 23, in <module>
    print(5/0)
ZeroDivisionError: division by zero


Using a try-except Block 

Try-except is where you tell Python to try running some code, and you 
tell it what to do if the code results in a particular kind of exception. 

"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")