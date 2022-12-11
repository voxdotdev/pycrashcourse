
'''
Modulo Operator

A tool for working with numerical info is the modulo operator (%)

It divides one number by another number and returns the remainder.

When one number is divisible by another number, the remainder is always 0. 
You can use this to determine if a number is even or odd. 

'''


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n The number {number} is even.")
else:
    print(f"\n The number {number} is odd.")