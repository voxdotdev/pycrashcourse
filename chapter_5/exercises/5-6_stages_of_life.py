
"""
5-6. Stages of Life: 
Write an if-elif-else chain that determines a person's stage of life. 
Set a value for the variable age, then:

• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.

"""

# NOTE: the type casting used here was not reviewed in the book, simply added for the exercise to be more useful.

age = input("How old are you? ")
age = int(age) 

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
elif age >= 65:
    print("You're an elder!")