"""
Let's build on this example and see how exception handling can help
when you're working with more than one file.


Let's pull in the text of Alice in Wonderland and try to count the number of
words in the text. We'll use the string method split() which can build a list
of words from a string.

"""

title = "Alice in Wonderland"
print(title.split())

""" 
OUTPUT: ['Alice', 'in', 'Wonderland'] 

The split() method separates a string into parts wherever it finds a space 
and stores all the parts of the string in a list. 

The result is a list of words from the string, although some punctuation may
also appear with some of the words. 

To count the number of words in Alice in Wonderland, we'll use split() on the 
entire text. Then, we'll count the items in the list to get a rough idea of 
the number of words in the text. 
"""

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")