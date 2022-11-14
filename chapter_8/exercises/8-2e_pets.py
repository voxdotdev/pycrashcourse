'''
Default Values 
When writing a function you can define a DEFAULT VALUE for each parameter.

If an argument for a parameter is provided in the function call, Python uses 
the argument value. 

If not, Python uses the parameter's default value. 

So when you define a default value for a parameter, 
you can exclude the corresponding argument you'd usually write in the function call. 

Using default values can simplify your function calls and clarify the ways in which 
your functions are typically used. 

For example, if you notice most of the calls to describe_pet() are being used to describe 
dogs, you can set the default value of animal_type to 'dog'. Now anyone calling 
describe_pet() for a dog can omit that info.

'''

def describe_pet(pet_name, animal_type ='dog'):
    """ Display info about a pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name=input("What's your dog's name? "))

'''
Note that the order of the parameters had to be changed. 
Because the default value makes it unnecessary to specify a type of animal 
as an argument, the only argument left in the function call is the pet name. 

Python still interprets this as a positional argument, so if the function is called
with just a pet's name, that argument will matchup with the first parameter 
listed in the function's definition. This is the reason the first parameter needs to be a 
pet_name.

The simplest way to use this function now is to provide just a dog's name in the 
function call. 

'''
describe_pet('willie')