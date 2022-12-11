"""
Write a while loop that prompts user for their name. 


When they enter their name, print a greeting to the screen and add a line 
recording their visit in a file called guest_book.txt. 

Make sure each entry appears on a new line in the file. 

"""

filename = 'guestbook.txt'

while True:

    name = input("What is your name? ")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as f: 
            f.write(f"{name.title()}\n")
        print(f"Welcome, {name}. You've been added to the guest list.")