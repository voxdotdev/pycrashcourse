'''
Write a function called make_shirt() that accepts a size and the text 
of a message that should be printed on the shirt.

The function should print a sentence summarizing the size of the shirt and the message printed on it. 

3) Call the function once using positional arguments to make a shirt. 
4) Call the function a second time using keyword arguments. 
'''


def make_shirt(size, text):
    print(f"You've order a size {size} shirt with the text: {text.title()}")
    
# 3
make_shirt('large', 'gone fishing')
# 4
make_shirt(text='wish i was here', size='small')

