'''
Using as to Give a Function an Alias 

If the name of a function you're importing might conflict with an existing 
name in your program, or if the function name is long, you can use a short
unique alias for it. 

from module_name import function_name as fn


'''

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

