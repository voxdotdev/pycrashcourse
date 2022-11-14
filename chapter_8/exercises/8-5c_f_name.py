'''
Making an argument optional 

You can use default values to make an argument optional. 
A first attempt to include a middle name might look like this:
'''

def get_formatted_name(first_name, middle_name, last_name):
    """ Return a full name, neatly formatted """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

'''
However, middle names aren't always needed, and this function written as is would 
not work if you tried to call it with only a first name and a last name.

To make the middle name optional, we can give the middle_name arg an empty default value, move it to the end
of the list of parameters, and ignore the argument unless the user provides a value. 
'''

def get_formatted_name(first_name, last_name, middle_name=''):
    """ Return a full name, neatly formatted """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee') #2
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

'''
Python interprets non-empty strings as TRUE, so middle_name evaluates to True
if a middle name is provided. 

Calling this function with a first and last name is straightforward, however if we're using 
a middle name, we have to make sure the middle name is the last argument passed so Python will match up the 
positional arguments correctly. (2)

'''