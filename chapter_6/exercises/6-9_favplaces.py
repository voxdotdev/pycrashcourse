'''
1) Make dictionary called favorite_places.

2) Think of three names to use as keys in the dictionary,
store one to three favorite places for each person. 

Loop through the dictionary, print each person's name and their favorite places. 

'''

favorite_places = {
    'alex': ['hawaii', 'home'],
    'john': ['alaska', 'burger king'],
    'ralph': ['the beach', 'the zoo']
}

# For the loop, assign each key to the variable after for, assign each dictionary to the second variable.
for people, places in favorite_places.items():
    print(f"\n{people.title()}:")
    for place in places:
        print(f"{place.title()}")