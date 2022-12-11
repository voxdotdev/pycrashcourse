import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
When Python reads this file, the line import pizza tells Python to open the file 
pizza.py and copy all the functions from it into this program. Python copies the code
behind the scenes before teh program runs. 

To call a function from an imported module, enter the name of the module you imported, 
pizza, followed by the name of the function, make_pizza(), separated by a dot. 

This first approach to importing, in which you simply write import followed by the name 
of the module, makes every function from the module available in your program. 

If you use this kind of import statement to import and entire module named 
module_name.py, each function in the module is available through the following syntax:

module_name.function_name()
'''