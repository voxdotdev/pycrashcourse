def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')


# Multiple Function Calls 
# Just calling the same function again with different definitions for keywords.
describe_pet('dog', 'willie')


# Via Keyword Arguments instead of Positional arguments
# Removes the possibility of mixing up definitions, order no longer matters.

describe_pet(animal_type='hamster', pet_name='harry')

# default value as parameter

def describe_pet2(pet_name, animal_type='dog'):
    """ display information about pets """
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet2(pet_name='willie')

# testing declared parameter override via argument

def describe_pet3(pet_name, animal_type='dog'):
    """ display information about pets """
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet3(animal_type='hamster', pet_name='henry')

