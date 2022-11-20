from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())



"""
Using Aliases

You can use aliases when importing classes as well. 

from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
As opposed to:
my_tesla = ElectricCar('tesla', 'roadster', 2019)

"""
