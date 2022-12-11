"""
Working with a File's Contents

After you've read a file into memory, you can do whatever you want with 
that data. First we'll attempt to build a single string containing all 
the digits in the file with no whitespace.
"""

filename = 'pi_digit.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


"""
Python reads all imported text as a string. If you want to work with a numerical
value you'll need to convert it to an int using the int() function or convert it
to a float using the float() function. 

"""