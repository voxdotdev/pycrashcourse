'''
Passing information to a function 

Modified slightly, the function greet_user can not only tell the user Hello! 
but also greet them by name. 

For the function to do this, you enter username in the parentheses of the function's definition 
at def greet_user(). 

By adding username here you allow the function to accept any value of username you specify. 

The function now expects you to provide a value for username each time you call it. 
When you call greet_user(), you can pass it a name, such as 'jesse' inside the parentheses:

'''


def greet_user(username):
    ''' Display a simple greeting. '''
    print(f"Hello, {username.title()}!")

greet_user(input("What is your name? "))