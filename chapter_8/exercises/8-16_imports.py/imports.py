'''
Using a program you wrote that has one function in it, store that function 
in a separate file. 

Import the function into your main program file, and call the function 
using each of these approaches:

import module_name
from module_name import function_name 
from module_name import function_name as fn
import module_name as mn 
from module_name import *

'''
import functions

functions.make_pizza(12, 'bacon', 'another pizza')

from functions import make_pizza

make_pizza(12, 'rice', 'another pizza')

from functions import make_pizza as fn

fn(12, 'mustard', 'another pizza')

import functions as mn

mn.make_pizza(12, 'bacon', 'another pizza')

from functions import *

make_pizza(12, 'bacon', 'another pizza')