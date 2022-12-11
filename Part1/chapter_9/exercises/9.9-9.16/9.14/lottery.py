"""
Make a list or tuple containing a series of 10 numbers and five letters.

Randomly select four numbers or letters from the list and print a message
saying that any ticket matching these four numbers or letters wins a prize.


"""

from random import choice

pool = [8,6,7,5,3,0,9,4,1,2,'A','B','C','D','E']

print("This is the winning combo this week:")
for num in range(4):
    winning_combo = choice(pool)
    print(winning_combo)
