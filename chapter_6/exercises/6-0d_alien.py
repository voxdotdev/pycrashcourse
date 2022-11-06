# move the alien to the right 
# determine how far to move the alien based on its current speed

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position: {alien_0['x_position']}")

# start exercise deviation for understanding 

alien_0['speed'] = 'fast'
print(f"Current speed: {alien_0['speed']}")

# end exercise deviation

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment. 

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")