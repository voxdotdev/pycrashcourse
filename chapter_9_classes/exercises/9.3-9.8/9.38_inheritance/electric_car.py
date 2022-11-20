'''
You don't always have to start from scratch when writing a class. 

If the class you're writing is a specialized version of another class 
you wrote, you can use inheritance. When one class inherits from another, 
it takes on the attributes and methods of the first class. 

The original class is called the parent class and the new class is the 
child class. 

The child class can inherit any or all of the attributes and methods of its 
parent class, but it's also free to define new attributes and methods of its own.

The __init__() Method for a Child Class

When you're writing a new class based on an existing class, you'll often 
want to call the __init__() method from the parent class. This will initialize
any attributes that were defined in the parent __init__() method and make them
available in the child class. 

For example, an electric car is just a specific kind of car, so we can base 
our new ElectricCar on the Car class we wrote earlier. 

Then we'll only have to write code for the attributes and behavior specific to 
electric cars.

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
        """ Initialize attributes of the parent class. """
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())


'''
When you create a child class, the parent class must be part of the current file and 
must appear before the child class in the file.

The super function is a special function that allows you to call a method
from the parent class. This line tells Python to call the __init__() method 
from Car, which gives an ElectricCar instance all the attributes defined in that method.

The name super comes from a convention of calling the parent class a superclass and the 
child a subclass. 

'''