"""
Is your Birthday Contained in Pi?

Let's use the program we just wrote to find out if someone's birthday
appears anywhere in the first million digits of pi. 

We can do this by expressing each birthday as a string of digits and seeing if 
that string appears anywhere in pi_string:

"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
    
print(f"{pi_string[:52]}...")
print(len(pi_string))