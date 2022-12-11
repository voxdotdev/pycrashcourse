"""
Large Files: One Million Digits

If we start with a text file that contains pi to 1,000,000 decimal places 
instead of just 30, we can create single string containing all these digits. 

We don't need to change our program at all except to pass it to a different file.

We'll also print just the first 50 decimal places, so we don't have to watch a 
million digits scroll by in the terminal: 
"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))