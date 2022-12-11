""" 
Write a while loop that asks people why they like 
programming. 

Each time someone enters a reason, add their reason to a file 
that stores all the responses. 

"""

filename = 'motive.txt'

while True:

    name = input("What is your name? ")

    if name == 'q':
        break
    else:
        reason = input("What do you like about programming? ")
        san_reason = reason.capitalize()
        san_name = name.title()
        with open(filename, 'a') as f: 
            f.write(f"Name: {san_name}\nReason: {san_reason}\n")

        print(f"Hey {san_name}, your motivation to code is '{san_reason}'?" \
        " I can appreciate that.")

