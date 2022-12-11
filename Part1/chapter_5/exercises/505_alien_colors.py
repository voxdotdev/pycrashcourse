# 5-5. Alien Colors #3
## Turn the if-else chain from 5-4 into an if-elif-else chain 
## If alien is green, print 5 points 
## If alien is yellow, print 10 points 
## If alien is red, print 15 points 
## Write 3 versions of this program, making sure each message is printed for the appropriate color alien

#1

alien_color = "green"

if alien_color == 'green':
    print(f"You've just earned 5 points for shooting a {alien_color} alien!")
elif alien_color == 'yellow':
    print(f"You've just earned 10 points for shooting a {alien_color} alien!")
else:
    print(f"You've just earned 15 points for shooting a {alien_color} alien!")


#2

alien_color = "yellow"

if alien_color == 'green':
    print(f"You've just earned 5 points for shooting a {alien_color} alien!")
elif alien_color == 'yellow':
    print(f"You've just earned 10 points for shooting a {alien_color} alien!")
else:
    print(f"You've just earned 15 points for shooting a {alien_color} alien!")

#3

alien_color = "red"

if alien_color == 'green':
    print(f"You've just earned 5 points for shooting a {alien_color} alien!")
elif alien_color == 'yellow':
    print(f"You've just earned 10 points for shooting a {alien_color} alien!")
else:
    print(f"You've just earned 15 points for shooting a {alien_color} alien!")