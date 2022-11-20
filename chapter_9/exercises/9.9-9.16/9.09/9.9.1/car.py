'''
Importing Classes 

As you add more functionality to your classes, your files can get long, even 
when you use inheritance properly. In keeping with the overall philosophy of 
Python, you'll want to keep your files as uncluttered as possible. 

To help, Python lets you store classes in modules and then import the classes 
you need into your main program. 

Importing a Single Class

Let's create a module containing just the Car class. This brings up a subtle
naming issue: we already have a file named car.py in this chapter, but this 
module should be named car.py because it contains code representing a car. 

We'll resolve this naming issue by storing the Car class in a module named car.py,
replacing the car.py file we were previously using. 

From now on, any program that uses this module will need a more specific filename,
such as my_car.py. Here's car.py with just the code from the class Car:

'''

""" A class that can be used to represent a car. """

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
        long_name =f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading. """
        self.odometer_reading += miles

""" Now we make a separate file called my_car.py. 
This file will import the Car class and then create an instance from that class. """

# B 

class Battery:
    """ A simple attempt to model a battery for an electric car. """

    def __init__(self, battery_size=75):
        """ Initialize the battery's attributes. """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """ Print a statement about the range this battery provides. """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """ 
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

""" Now we can make a new file called my_electric_car.py, import the ElectricCar
class, and make an electric car."""