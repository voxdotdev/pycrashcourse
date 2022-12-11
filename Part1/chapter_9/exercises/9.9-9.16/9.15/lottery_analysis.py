"""
You can use a loop to see how hard it might be to win the kind of lottery 
you just modeled. 

Make a list or tuple called my_ticket. 

Write a loop that keeps pulling numbers until your ticket wins. 

Print a message reporting how many times the loop had to run to give you 
a winning ticket. 

"""
from random import choice

# Function to generate winning ticket 

def get_winning_ticket(pool):

    winning_ticket = []
    while len(winning_ticket) < 4:
        winning_pull = choice(pool)
        if winning_pull not in winning_ticket:       
           winning_ticket.append(winning_pull)

    return winning_ticket

# Function to check winning ticket against user's ticket

def winner_check(my_ticket, winning_ticket):
    for num in my_ticket:
        if num not in winning_ticket:
            return False

    return True, num

def make_entry_ticket(pool):
    my_ticket = []
    while len(my_ticket) < 4:
        winning_pull = choice(pool)
        if winning_pull not in my_ticket:
            my_ticket.append(winning_pull)

    return my_ticket

pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(pool)


turn = 0
won = False
max_tries = 1_000_000


while not won: 
    new_ticket = make_entry_ticket(pool)
    won = winner_check(winning_ticket, new_ticket)
    turn += 1
    if turn >= max_tries:
        break

if won:
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {turn} tries to win!")

else:
    print(f"Tried {turn} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")


# This script would not produce a winner unless 
# the while not won was modified as shown here. 
# something to do with the pseudorandom Random module algorithm