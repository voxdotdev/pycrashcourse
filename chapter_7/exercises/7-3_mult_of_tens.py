'''
Ask the user for a number, then report whether the number is a multiple of 10 or not.
'''


num = input("Enter a number and I'll tell you if it's a multiple of 10: ")
num = int(num)


if num % 10 == 0:
    print(f"\n{num} is a multiple of 10.")
else:
    print(f"\n{num} is not a multiple of 10.")