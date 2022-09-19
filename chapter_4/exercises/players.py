# Slicing a list 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Any subset can be generated 

print(players[1:4])

# Omitting the first index in a slice
# starts the slice at the beginning of the list

print(players[:4])

# Looping through a slice 

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())