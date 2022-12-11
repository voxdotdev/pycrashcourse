"""
Working with Multiple Files

Let's add more books to analyze, but first move the bulk of 
this program to a function called count_words(). 

"""

def count_words(filename):
    """ Count the approximate number of words in a file. """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

"""
Now we can write a simple loop to count the words in any text we want to analyze.
"""

filenames =  ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)