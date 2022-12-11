# Making Numerical Lists 
## Lists are ideal for storing sets of numbers
## Using the range() function, prints 1-4. 

for value in range(1,5):
    print(value)


for value in range(1,6):
    print(value)


# range() can also be passed with one value, output is 0-5

for value in range(6):
    print(value)

# Use range() to make a list of numbers 

numbers = list(range(1,6))
print(numbers)