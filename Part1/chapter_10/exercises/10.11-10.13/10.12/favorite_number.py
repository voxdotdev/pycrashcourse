"""
Write a program that prompts for the user's favorite number. 

Use json.dump() to store this number in a file. 

Write a separate program that reads in this value and prints the message,
"I know your favorite number! It's ____."

# Looking back, this is actually 10.12, 10.11 asks for two separate files.
However It's redundant for the sake of understanding, which I feel confident I do.

"""
import json

# get new user input fav number
def get_new_favnum():
    """ Prompt user for their favorite number. """
    fav_number = input("What is your favorite number? ")
    filename = 'favnum.json'
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
    return fav_number

# retrieve user input fav number 
def get_stored_favnum():
    """ Get stored favorite number if available. """
    filename = 'favnum.json'
    try:
        with open(filename, 'r') as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else: 
        return fav_num

# greet user with fav number
def greet_user():
    """ Greet the user with their fav number. """
    fav_number = get_stored_favnum()
    if fav_number:
        print(f"I know your favorite number! It's {fav_number}.")
    else:
        get_new_favnum()
        print(f"We'll remember your favorite number when you come back!")

greet_user()