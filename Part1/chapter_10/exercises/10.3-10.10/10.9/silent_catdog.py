"""
Modify your except block from 10.8 to fail silently if either file is missing.
"""

def read_names(filename):

    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
    


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_names(filename)
