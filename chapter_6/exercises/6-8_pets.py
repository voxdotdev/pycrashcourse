'''
1) Make several dictionaries, where each dictionary represents a different pet.

2) In each dictionary, include the kind of animal and the owner's name. 

3) Store these dictionaries in a list called pets. 

4) Next, loop through your list and as you do, print everything you know about each pet. 

'''

pets = {
    'pet1': {'name': 'penelope', 'type': 'horse', 'owner': 'doug'},
    'pet2': {'name': 'felix', 'type': 'cat', 'owner': 'sam'},
    'pet3': {'name': 'ralph', 'type': 'monkey', 'owner': 'george'},
}

for pet, pet_info in pets.items():
    overview = f"{pet_info['name']} is a {pet_info['type']}"
    owner =  f"{pet_info['owner']}"
    print (f"\t {overview.capitalize()}, they belong to {owner.title()}.")

