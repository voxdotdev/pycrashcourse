from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

"""
Even though we called battery here, we don't have to import the battery class
because the ElectricCar class already calls it in car.py via self.battery = Battery()

Importing Multiple Classes from a Module 

You can import as many classes as you need into a program file. 
See my_cars.py
"""