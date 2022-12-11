""" 
Make a class Die with one attribute called sides, which has a default
value of 6. 

Write a method called roll_die() that prints a random number between 1 
and the number of sides the die has. 

Make a 6-sided die and roll it 10 times. 

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint

class Die:

    def __init__(self):

        self.sides = 6

    def roll_die(self):

        re_roll = range(1,11)

        print(f"Rolling a {self.sides} sided die 10 times: ")
        for num in re_roll:
            output = randint(1, self.sides)
            print(f"{num}: {output}")

start = Die()
start.roll_die()
start.sides = 10
start.roll_die()
start.sides = 20
start.roll_die()

""" Exercise 9-13, this time actually following the instructions, I think anyway. """