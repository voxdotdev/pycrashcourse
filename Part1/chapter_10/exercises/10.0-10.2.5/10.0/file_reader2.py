"""
Reading Line by Line

You might want to read through a file of data and work with any line 
that includes a specific keyword, or html tag. You can use a for loop 
on the file object to examine each line from a file one at a time.

"""
filename = 'pi_digit.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

""" This generates more blank lines than before however, due to an invisible newline
character at the end of each line in the text file. rstrip resolves this. """
