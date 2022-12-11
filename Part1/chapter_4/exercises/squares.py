## Make a list of the first 10 square numbers
## the square of each integer from 1 through 10
## In python ** represents exponents

# Start with an empty list 
squares = []

# For loop to loop through each value from 1 to 10 using range()
for value in range(1, 11):
    # Inside the loop, the current value is raised to the 2nd power. 
    # and assigned to the variable square. 
    square = value ** 2
    # Each new value of square is appended (added to the end) of squares list
    squares.append(square)

# Once the loop is complete the list is printed.
print(squares)


## List comprehensions 
# comprehension allows the generation of the same list using one line of code
# by combining the for loop and the create of new elements into one line, 
# then automatically appending each new element

print("List Comprehensions Example")

squares = [value**2 for value in range(1,11)]
print(squares)