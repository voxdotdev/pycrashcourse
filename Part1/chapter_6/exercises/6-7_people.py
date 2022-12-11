'''
1) Start with the program you wrtoe for Exercise 6-1.

2) Make two new dictionaries representing different people, store all three dictionaries in a list called people. 

3) Loop through your list of people. 
As you loop through the list, print everything you know about each person. 

'''

# Program from 6-1
person_A = {'first_name': 'Green','last_name': 'Goblin','age': '42?','city': 'New York'}
#2
person_B = {'first_name': 'The', 'last_name': 'Pope', 'age': 'Elderly', 'city': 'vatican'}

person_C = {'first_name': 'a', 'last_name': 'baby', 'age': 'new born', 'city': 'stork city'}

people = [person_A, person_B, person_C]
#3
for person in people:
    print(person)