'''
Nesting Dictionaries

Sometimes you'll want to store multiple dictionaries in a list.
This is called nesting. 

You can nest dictionaries inside of a list, a list of items inside of
a dictionary, even a dictionary inside of another dictionary.

A List of Dictionaries 

The alien_0 dictionary contains a variety of information about one alien,
but it has no room to store more information about a second alien, much 
less a screen full of them. 

One way to accomodate for this is to make a list of aliens 
in which each alien is a dictionary of information about that alien.

'''

alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

''' a more practical example that generates each alien via range'''

aliens = []

# Make 30 green aliens 
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

#  Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

''' 
Imagine one aspect of the game has some aliens changing color and 
moving faster as the game progresses. When it's time to change 
colors, we can use a for loop and an if statement to change the 
color of aliens. 
'''

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#  Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")