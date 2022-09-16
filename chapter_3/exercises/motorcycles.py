motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[0],motorcycles[1],motorcycles[2])

# Change the first item in the list from honda to ducati

motorcycles[0] = 'ducati'
print(motorcycles[0],motorcycles[1],motorcycles[2])

# Change the last item in the list from suzuki to moped

motorcycles[-1] = 'moped'
print(motorcycles[0],motorcycles[1],motorcycles[2])

## Appending Elements to the End of a List
motorcycles.append('ducati')
print(motorcycles)

# Using an empty list, add the elements honda yamaha and suzuki to the list

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Insert a new value, ducati, at 0. 

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Delete Honda from the list below

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)

# Delete Yamaha from the list below 

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[1]
print(motorcycles)

# Pop a motorcycle from the list of motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Another example of POP. Last owned motorcycle

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Pop an item from any position in the list 

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Remove an item from the list using the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')

print(motorcycles)

# Further example of using remove() method
# Removing via a variable removes the item from the list but
# makes it so the item is still accessible through the variable too_expensive 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# Avoiding index errors 
# -1 will always return the last item in a list
# the only time this will result in an error is if the list is empty
# list = []
print(motorcycles[-1])