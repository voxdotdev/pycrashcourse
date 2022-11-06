"""
Write a function called make_shirt() that accepts a size and the text of a message that
should be printed on the shirt. The function should print a sentence summarizing the 
size of the shirt and the message printed on it. 

Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments. 

"""

def make_shirt(size, message):
    print(f"You've ordered a {size} shirt with the message '{message}' - I hope you're happy. No refunds.\n")

# Postional Arguments - pass the argument, using only the default order of the parameters

make_shirt('medium', 'Eat fresh.')

# Keyword Arguments - pass the argument, specifying which parameter to use

make_shirt(size='medium', message="There's a snake in my boot!")
