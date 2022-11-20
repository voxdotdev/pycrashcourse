'''
Working with Classes and Instances 

You can use classes to represent many real-world situations. 

Once you write a class, you'll spend most of your time working with 
instances created from that class. 

One of the first tasks you'll want to do is modify the attributes associated with 
a particular instance. You can modify the attributes of an instance directly or 
write methods that update attributes in specific ways. 

The Car Class 
Our class here will store information about the kind of car we're working with, and it 
will have a method that summarizes this information: 
'''

class Car:
    """ A simple attempt to represent a car. """


    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())