"""
Failing silently

In the previous example we informed our users that one of the files was
unavailable. But you don't need to report every exception you catch. 

To make a program fail silently, you write a try block as usual, but you 
explicitly tell Python to do nothing in the except block. 

Python has a pass statement that tells it to do nothing in a block called pass.
"""

def count_words(filename):
    """ Count the approximate number of words in a file. """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass # fail silently 
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames =  ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


"""
Pass is also good as a placeholder, for when you want to do something later.
For example, in this program we might decide to write any missing filenames to 
a file called missing_files.txt. 

"""