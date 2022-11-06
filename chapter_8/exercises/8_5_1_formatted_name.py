# Function that takes a first and last name, then returns a neatly formatted full name

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Making an argument optional, if a third, middle name argument is present,
# either positional or keyword, great, print full name including middle name. 
# if not, that's great too, print full name without.
# by accounting for the choice we remove the possibility of error from omission.

def get_formatted_name2(first_name, last_name,  middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)