'''
Creating and Using a Class

In this example we'll create a class for a dog, containing traits / attributes that 
apply to all dogs, such as name, age, tricks. 

After our class is written, we'll use it to make individual instances, each of which 
represents one specific dog.

Each instance created from the Dog class will store a name and an age, and we'll give 
each dog the ability to sit() and roll_over():

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


'''
By convention, capitalized names refer to classes in Python. There are no parentheses 
in the class definition because we're creating this class from scratch.

The __init__() Method

A function that's part of a class is a Method. Everything learned so far about functions
also applies to methods. The only practical difference for now is the way methods are called. 

The __init__() method is a a special method Python runs automatically whenever we create a 
new instance based on the Dog class. This method has two leading underscores and two trailing 
underscores, a convention to help prevent Python's default method names from conflicting
with your method names. 

We define the __init__() method to have three parameters, self, name, and age.
The self parameter is required in the method definition, and it must come first before the
other parameters. It must be included in the definition because when Python calls this method
later on, to create an instance of Dog), the method call will automatically pass the self 
argument. 

Every method call associated with an instance automatically passes self, which is a reference to 
the instance itself. It gives the individual instance access to the attributes and methods in the class.

When we make an instance of Dog, Python will call the __init__() method from the Dog class. 
We'll pass Dog() a name and an age as arguments; self is passed automatically.

Whenever we want to make an instance from the Dog class, we'll provide the values for only the last
two parameters, name and age.

The two variables defined within __init__() both have the prefix self. Any variable prefixed
with the self is available to every method in the class. We'll also be able to access these variables 
through any instance created from the class. 

The line self.name = name takes the value associated with the parameter NAME, and assigns it to the 
variable name, which is then attached to the instance being created. The same process happens with 
self.age = age. Variables that are accessible through instances like this are called attributes. 

'''

