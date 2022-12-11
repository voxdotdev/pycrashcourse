'''
Overriding Methods from the Parent class 

You can override any method from the parent class that doesn't fit what you're
trying to model with the child class. 

To do this you define a method in the child class with the same name as the 
method you want to override in the parent class. 

Python will disregard the parent class method and only pay attention to the method 
you define in the child class. 

Say the class Car had a method called fill_gas_tank(). This method is meaningless
for an all-electric vehicle, so you might want to override this method. 
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

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the give value. 
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading. """
        self.odometer_reading += miles

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """ 
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """ Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank():
        """ Electric cars don't have gas tanks. """
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


'''
By defining a new method in the child class with the same name as the the method from the parent 
class, you overwrite it essentially. Python will ignore the parent method and run this one
instead. 

'''

