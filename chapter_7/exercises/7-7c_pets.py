'''
Removing All Instances of Specific Values from a List 

In Chapter 3 we used remove() to remove a specific value from a list. 
The remove function worked because the value we were interested in appeared
only once in the list. But what if you want to remove all instances of a value? 

Say you have a list of pets with the value 'cat' repeated several times. 
To remove all instances of that value, you can run a while loop until 'cat'
is no longer in the list, as shown here: 

'''

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)