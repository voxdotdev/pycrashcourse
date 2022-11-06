"""
modify makeshirt() from 8-2 exercise so that shirts are large by default 
with a message that reads 'I love Python' 
Make a large shirt and a medium shirt with the default messsage. 
Make a shirt of any size wiht a different message

"""

def makeshirt(size='large', message='I love Python'):
    print(f"You've ordered a {size} size shirt reading: {message} - Hurrah for you. Still no refunds.")

makeshirt()
makeshirt('medium')

makeshirt('small', 'I took a Python course and all I got was this awesome T-shirt')
