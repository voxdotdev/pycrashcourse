'''
Multiple Function Calls 

You can call a function as many times as needed. 
Describing a second, different pet requires just one more call to describe_pets(): 

'''

def describe_pet(animal_type, pet_name):
    """ Display info about a pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(input('type of pet: '), input('name of pet: '))


'''
You can use as many positional arguments as you need in your functions. 
Python works through the arguments you provide when calling  the function
and matches each one with the corresponding parameter in the function's definition.
'''