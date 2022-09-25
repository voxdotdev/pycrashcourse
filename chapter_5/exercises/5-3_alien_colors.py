# 5-3. Alien Colors #1 
## Imagine an alien was just shot down in a game.
## Create a variable called alien_color 
## Assign it a value of green, red, or yellow 

alien_color = 'green'

print(f"Woah, you shot down a {alien_color} alien!")

## Write an if statement to test whether the alien's color is green.
## If it is, print a message that the player just earned 5 points.

if alien_color == 'green':
    print("You've just earned 5 points!")

## Write on version of this program that passes the if test 
## and another that fails. The version that fails will have no output

if alien_color != 'green':
    print("I'm blue dabadee")