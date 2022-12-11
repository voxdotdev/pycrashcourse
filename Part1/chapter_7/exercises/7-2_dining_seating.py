'''
Write a program that asks the user how many people are in their dinner group.

If the answer is more than 9, print a message saying they'll have to wait for a table.

Overwise, report that their table is ready.

'''

party = input("How many people are in your dining party? ")
party = int(party)

if party > 9:
    print("That's a large group! Please have a seat until we call you.")
else:
    print("Your table is ready, please follow me this way.")