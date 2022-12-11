'''
A function can return any kind of value you need it to, including more complicated data 
structures like lists and dictionaries. 

For example, the following function takes in parts of a name and returns a dictionary representing a person:

'''

def build_person(first_name, last_name):
    """ Return a dictionary of information about a person """
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

'''
You can extend this function to accept optional values like a middle name, an age, occupation, 
any other information you'd want to store about a person. For example, storing a person's age: 
'''
def build_person(first_name, last_name, age=None):
    """ Return a dictionary of information about a person """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

'''
Like an argument containing a value resulting to true, if it contains None specifically it evaluates to false. 
Empty arguments and the None keyword both evaluate the same, false, but None is a special keyword that can be referenced. 
'''