# In Python, square brackets [] indicate a list
# and individual elements in the list are separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# output ['trek', 'cannondale', 'redline', 'specialized'] 
# Because this output isn't formatted for readability, 
# it's better to access individual list items.


# Accessing Elements in a List 

print(bicycles[0])

# The string methods from Chapter 2 can also be applied for further formatting.

print(bicycles[0].title())

# Access the last item in the list

print(bicycles[-1])

# Access the second to last item in the list, and so on. 

print(bicycles[-2])

# Using values from a list in a string 

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)