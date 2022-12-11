"""
Refactoring 

You'll get to a point where your code will work, but you'll recognize
that you could improve the code by breaking it up into a series of functions
that have specific jobs. This process is called refactoring.

Refactoring makes your code cleaner, easier to understand, and easier to extend.

We can refactor remember_me.py by moving the bulk of its logic into one or more
functions. The focus of remember_me.py is on greeting the user, so a greet_user()
function would be appropriate.
"""

import json

def greet_user():
    """ Greet the user by name. """
    filename = 'username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username.title()}!")

greet_user()