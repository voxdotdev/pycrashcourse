""" Saving and Reading User-Generated Data """

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

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