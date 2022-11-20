'''

Args and Params 

The information supplied to a function are called arguments.
The variables defined in parentheses are called parameters.
We supply arguments to populate these parameters.


Write a function called display_message() that prints one sentence 
telling everyone what you are learning in this chapter. 
Call the function, make sure the message displays correctly.

'''

def display_message(topic):
    print(f"{topic.title()}, what fun!")

display_message(input("What are you learning about in this chapter? "))
