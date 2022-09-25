# 5-4. Alien Colors #2
## Choose a color for an alien as done in Exercise 5-3

## Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'

alien_color = "green"

print(f"Woah, you shot down a {alien_color} alien!")

## Write an if statement to test whether the alien's color is green. 
## If so, print a message that the player just earned 5 points. 
##  If the alien’s color isn’t green, print a statement that the player just earned 10 points.
## Write one version of this program that runs the else block

if alien_color == "green":
    print("You've just earned 5 points!")
else:
    print("You've just earned 10 points!")

## Write one version of this program that runs the if block

if alien_color == "green":
    print("You've just earned 5 points!")
if alien_color != "green":
    print("You've just earned 10 points!")