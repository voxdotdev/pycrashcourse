"""
Importing an Entire Module 

You can also import an entire module and then access the classes you need 
using dot notation. This approach is simple and results in code that is easy 
to read. 

Because every call that creates an instance of a class includes the module name,
you won't have naming conflicts with any names used in the current file.

Here's what it looks like to import the entire car module and then create a 
regular car and an electric car: 
"""

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


"""
Importing all Classes from a Module 

from module_name import *

This method is not recommended for two reasons. First, it's helpful to be
able tto read the import statements at the top of a file and get a clear sense
of which classes a program uses. This approach can also lead to confusion with 
names in the file. If you accidentally import a class with the same name as something
else in your program file, you can create errors that are hard to diagnose. 

If you need to import many classes from a module, you're better off importing 
the entire module and using the module_name.ClassName syntax. 

You won't see all the classes used at the top of the file, but you'll see clearly 
where the module is used in the program, as well as avoid aforementioned naming 
conflicts. 

"""