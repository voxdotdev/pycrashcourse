# 4-7. Threes 
## Make a list of the multiples of 3 from 3 to 30. 
## Use a for loop to print the numbers in the list 

threes = []
for value in range(1,31):
    three = value*3
    print(three)
    threes.append(three)

print(threes) # not directed, just to see all in list for confirmation.