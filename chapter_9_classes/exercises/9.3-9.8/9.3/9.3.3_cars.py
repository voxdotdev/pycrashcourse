'''
Setting a Default Value for an Attribute

When an instance is created, attributes can be defined without being
passed in as parameters. These attributes can be defined in the __init__()
method, where they are assigned a default value. 

Here we're adding an attribute called odometer_reading that always starts with a 
value of 0. We'll also add a method read_odometer() that helps us read each car's odometer.
'''


class Car:
    """ A simple attempt to represent a car. """


    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it.")

    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()