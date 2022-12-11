# 3-8 Seeing the World
## Store the locations of at least five popular vacation places
# in the world, making sure the list is not in alphabetical order.

from audioop import reverse


places = ['London', 'Paris', 'Tokyo', 'Rome', 'Prague']

# Print the list in its original order, raw format

print(places)

# Use sorted() to print the list in alphabetical order 
# without modifying actual list 

print(f"Temporary sort: {sorted(places)}")

# Show the list is still in the original order by printing 

print(f"Original order: {places}")

# Use reverse() to change the order of the list. 
# Print the list to show that the order has changed. 
  

places.reverse()
print(f"Reversed order: {places}")

# Use reverse() to change the order back, print again.

places.reverse()
print(f"Original order: {places}")

# Use sort to sort the list permanently. Print to show.

places.sort()
print(f"Sorted order: {places}")

# Use sort to sort the list in reverse alphabetical order, print.

places.sort(reverse=True)
print(f"Sorted Reverse order: {places}")

# 3-9 Dinner Guests - see guest_list.py