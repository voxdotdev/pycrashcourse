"""
One excellent resource for exploring the Python standard library is 
a site called Python Module of the Week.

Go to https://pymotw.com/ and look at the table of contents. 

Find a module that looks interesting to you and read about it, 
perhaps starting with the random module.


"""
import string
from pprint import pprint

# Text - String
# Formatting text 

s = 'The quick brown fox jumped over the lazy dog.'

print(s)
print(string.capwords(s))


# Data Structures - PPrint - Pretty Print 
# Prettifying complex lists / dictionaries.

data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]


print('PRINT:')
print(data)
print()
print('PPRINT:')
pprint(data)