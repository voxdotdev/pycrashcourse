'''
Importing All Functions in a Module

You can tell Python to import every function in a module by using the asterisk *
'''

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers','extra cheese')

'''
Because every function is imported, there is no need to reference the module name. 
It's best not to use this approach when you're working with larger modules that you 
didn't write.

The best approach is to import the functions you want, or import the entire module 
and use the dot notation. 
'''