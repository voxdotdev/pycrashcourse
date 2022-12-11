""" 
Refactoring Continued

We refactored a little in 7.remember_me.py, however our greet function is
still doing more than greeting the user, reading from a file,
so we should refactor further.

"""

import json

def greet_user():
    """ Greet the user by name. """
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}!")
    else:
        username = input("What is your name? ")
        filename = "username.json"
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    

def get_stored_username():
    """ Get stored username if available. """
    filename = "username.json"
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

greet_user()


""" A function should either return the value you're expecting, or return None."""