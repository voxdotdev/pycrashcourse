'''
What is a function 
A block of code, or black box, designed to do one specific job. 
When you wan to perform a particular task that you've defined in a function, 
you CALL the function responsible for it. 

If you need to perform that task multiple times throughout your program, you don't need 
to type all the code for the same task again and again; instead you just call the function
dedicated to handling that task, and the call tells Python to run the code inside the function. 

You'll find that using functions makes your programs easier to write, read, test, and fix. 

In this chapter you'll also learn ways to pass information to functions. 
You'll learn how to write certain functions whose primary job is to display information 
and other functions designed to process data and return a value or set of values. 

Finally, you'll learn to store functions in separate files called modules to help organize your main
program files.

'''

# Defining a Function 

def greet_user():
    ''' Display a simple greeting. '''
    print('Hello!')

greet_user()

'''
This example shows the simplest structure of a function. 
The keyword def informs Python that you're defining a function. 
This is the FUNCTION DEFINITION, which tells Python the name of the function
and if applicable, what kind of information the function needs to do its job. 
The parentheses holds that information. In this case the function does not 
need any info to do its job, so its parentheses are empty. 

Any indented lines that follow def make up of the BODY of the function. 
A comment inside of a function is known as a DOCSTRING, which describes what the function does. 
Enclosed in triple quotes, Python looks for these when it generates documentation for the functions
in your programs. 

The line print('Hello!') is actually the only line of code in the body of this function. 
Greet user just has one job, print hello. 

When you want to use a function, you call it. To CALL the function you write the name of the function, 
followed by any necessary information in parentheses. 
'''