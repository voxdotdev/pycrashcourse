'''
Avoiding Infinite Loops

Every while loop needs a way to stop running so it won't continue to run forever. 
For example, this counting loop should count from 1 to 5: 

'''

x = 1

while x <= 5:
    print(x)
    x += 1


# This loop runs forever! 
x = 1
while x <= 5:
    print(x)