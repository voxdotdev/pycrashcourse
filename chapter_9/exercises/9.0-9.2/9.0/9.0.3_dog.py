'''
After we create an instance from the class Dog, we can use the dot notation to call 
any method defined in Dog. Let's make our dog sit and roll over. 
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
my_dog.sit()
my_dog.roll_over()


'''
When Python reads my_dog.sit(), it looks for the method sit() in the class Dog
and runs that code. When attributes and methods have been given descriptive names 
we can easily infer what a block of code is supposed to do. 
'''

