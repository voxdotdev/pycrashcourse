
"""
Write a program that prompts the user for their name. 

When they respond, write their name to a file called guest.txt
"""


def check_in(name):

    """ Add guest name to file. """

    log = 'guest.txt'
    name = name.title()

    with open(log, 'w') as file_object:
        file_object.write(name)
    print(f"Hello, {name}. You've been checked in, enjoy your stay!")


check_in(input("Welcome, what is your name? "))

