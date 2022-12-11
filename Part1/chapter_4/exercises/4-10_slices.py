# 4-10. Slices
## Using one of the programs written in a previous exercise, 
## add several lines to the end of the program that do the following:
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'bob', 'mark', 'joel', 'tom']


## Print the message "The first three items in the list are:"
## Use a slice to print the first three items from that list. 

print("The first three players in the roster are:")
for player in players[:3]:
    print(player.title())

## Print the message "Three items from the middle of the list are:"
## Use a slice to print three items from the middle of the list.

print("Three players from the middle of the roster are:")
for player in players[3:6]:
    print(player.title())


## Print the message "The last three items in the list are:".
## Use a slice to print the last three items in the list.

print("The last three players in the roster are:")
for player in players[6:9]:
    print(player.title())