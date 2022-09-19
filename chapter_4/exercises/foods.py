## Copying a list 

# Declare a list called my_foods 
my_foods = ['pizza', 'falafel', 'carrot cake']

# Declare a new list and make a copy of my_foods 
# [:] specifies make a slice without specifying at indices,
# copying the entire contents of the list into the new list. 
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Prove there are two separate lists by adding a 
# new food to each list, show that each list keeps track
# of the appropriate peron's favorite food.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)