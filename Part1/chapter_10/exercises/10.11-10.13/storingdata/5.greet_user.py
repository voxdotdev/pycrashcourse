""" Reading Saved User-Generated Data """

import json

filename = 'username.json'
with open(filename, 'r') as f:
    username = json.load(f).title()
    print(f"Welcome back, {username}!")