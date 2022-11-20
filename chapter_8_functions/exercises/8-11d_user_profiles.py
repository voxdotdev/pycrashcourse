'''
Using Arbitrary Keyword Arguments 

Sometimes you'll want to accept an arbitrary number of arguments, but you won't 
know ahead of time what kind of information will be passed to the function. 

In this case, you can write functions that accept as many key-value pairs as the 
calling statement provides. 

One example involves building user profiles: 
you know you'll get information about a user, but you're not sure what kind of info
you'll receive. The function build_profile() in the following example always
takes in a first and last name, but it accepts an arbitrary number of keyword 
arguments as well.

'''


def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about a user. """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

'''
The definition of build_profile() expects a first and last name, and then it allows 
the user to pass in as many name-value pairs as they want. 

The double asterisks before the parameter **user_info cause Python to create an empty
dictionary called user_info, and pack whatever name-value pairs it receives into this 
dictionary. Within the function you can access the key-value pairs in user_info 
just as you would for any dictionary. 

This would work no matter how many additional key-value pairs are provided in the call.

Practice will teach when to use the different types of arguments correctly, for now 
remember to user the simplest approach that gets the job done. 

You'll often see the parameter name **kwargs used to collect non-specific keyword
arguments.

'''