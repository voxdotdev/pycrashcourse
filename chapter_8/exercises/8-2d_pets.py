'''
Keyword Arguments 

A KEYWORD ARGUMENT is a name-value pair that you pass to a function. 
You directly associate the name and the value within the argument. 
This way when you pass the argument to the function, there's no confusion. 

'''


def describe_pet(animal_type, pet_name):
    """ Display info about a pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(input())
