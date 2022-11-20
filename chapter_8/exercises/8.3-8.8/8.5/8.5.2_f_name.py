'''
Return Values 

Instead of outputting directly, a function can process data then return a value or set of values.
The value the function returns is called RETURN VALUE. The return statement takes a value from 
inside the function and sends it back to the line that called the function. 


'''

def get_formatted_name(first_name, last_name):
    """ Return a full name, neatly formatted """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

'''
This might seem like a lot of work to get a neatly formatted name when we could have just printed the name via one line. 
But consider working with a large program that needs to store many first and last names separately. Functions like 
get_formatted_name() become very useful. You store the first and last names separately and then call this function 
whenever you wan to display a full name. 

'''