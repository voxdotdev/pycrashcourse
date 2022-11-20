'''
Making an Instance from a Class 

Think of a class as a set of instructions for how to make an instance. 

The class Dog is a set of instructions that tells Python how to make 
individual instances representing specific dogs. 

Below we're making an instance representing a specific dog.
'''

class Dog:
    """ A simple attempt to model a dog. """

    def __init__(self, name, age):
        """ Initialize name and age attributes. """
        self.name = name
        self.age = age

    def sit(self):
        """ Simulate a dog sitting in response to a command. """
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """ Simulate a dog rolling over in response to a command. """
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

'''
In this case, my_dog is an instance of Dog. 
'''