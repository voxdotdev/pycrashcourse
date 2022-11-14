'''
Positional Arguments 

Python matches each argument in the function call with the a param
in the function definition. The simplest way to do this is based on the 
order of the arguments provided. 

Values matched up this way are called POSITIONAL ARGUMENTS.

Consider a function that displays information about pets.
The function tells us what kind of animal each pet is and the pet's name. 

'''

def describe_pet(animal_type, pet_name):
    """ Display info about a pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')