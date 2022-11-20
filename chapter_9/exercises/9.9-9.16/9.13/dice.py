""" 
Make a class Die with one attribute called sides, which has a default
value of 6. 

Write a method called roll_die() that prints a random number between 1 
and the number of sides the die has. 

Make a 6-sided die and roll it 10 times. 

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

#region imports
from random import randint
#endregion

class Die:

    def __init__(self):
        """ Initialize class and attribute range, 10 rolls max. """
        self.rolls = range(1,11)

    def roll(self, sides):
        """
        Roll method. Generate a random number between 1 and number of sides.
        Print both the iteration and each generated number up to range.
        """
        for num in self.rolls:
            outcome = (randint(1, sides))
            print(f"{num}: {outcome}")
            
    def six_sided(self):
        """ 6 sided die method to tell rolls method number of sides. """
        print("Rolling a 6 sided die: ")
        self.roll(6)

    def ten_sided(self):
        """ 10 sided die method to tell rolls method number of sides. """
        print("Rolling a 10 sided die: ")
        self.roll(10)

    def twenty_sided(self):
        """ 20 sided die method to tell rolls method number of sides. """        
        print("Rolling a 20 sided die: ")
        self.roll(20)

#region class initialization / method calls
roll = Die()
roll.six_sided()
roll.ten_sided()
roll.twenty_sided()
#endregion

""" .... I didn't follow the instructions. But it works! will revisit. """