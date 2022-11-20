from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

"""
Picture how long this program file would be if the entire Car class were included.

Storing Multiple Classes in a Module

You can store as many classes as you need in a single module, although each class 
in a module should be related somehow. 

The classes Battery and ElectricCar both help represent cars, so let's add them to the 
module car.py. (noted with 'B' for exercise work flow clarity.)

"""