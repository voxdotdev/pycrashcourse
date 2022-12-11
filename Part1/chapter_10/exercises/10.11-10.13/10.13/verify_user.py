"""
The final listing for remember_me.py in storingdata assumes either that 
the user has already entered their username, or that the program is running for 
the first time.

We should modify it in case the current user is not the person who last used
the program. 

Before printing a welcome back message in greet_user(), ask the user if this
is the correct username. If it's not, call get_new_username() to get the
correct username. 

"""

import json

def greet_user():
    """ Greet the user by name. """ 
    username = get_stored_username()

    if username:
        confirm = input(f"Is {username} the correct username? y/n ")
        if confirm == 'y':
            print(f"Welcome back, {username.title()}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username.title()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}!")
    # seems repetition like this indicates this should be refactored.

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

def get_new_username():
    """ Prompt for a new username. """
    username = input("What is your name? ").title()
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

greet_user()