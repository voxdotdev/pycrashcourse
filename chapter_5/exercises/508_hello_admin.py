"""
5-8. Hello Admin:

Make a list of 5 or more usernames, including the name 'admin'.
Loop through the list and print a greeting to each user:

* If the username is 'admin', print a special greeting acknowledging their rank.
* Otherwise, print a generic greeting along with the user logging in. 

"""

usernames = ['joey', 'phoebe', 'rachel', 'chandler', 'monica', 'admin', ]

for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in!")

"""
OUTPUT

Hello Joey, thank you for logging in!
Hello Phoebe, thank you for logging in!
Hello Rachel, thank you for logging in!
Hello Chandler, thank you for logging in!
Hello Monica, thank you for logging in!
Hello Admin, would you like to see a status report?

"""