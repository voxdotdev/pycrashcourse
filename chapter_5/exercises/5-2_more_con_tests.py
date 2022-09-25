# 5-2. More Conditional Tests

# Write more tests 
# Have at least one True and False result for each of the following:

# Test for equality and inequality with strings

animal = 'badger'

print("Is the animal a goat?")
print(animal == 'goat')

print("Okay, is it a badger?")
print(animal == 'badger')

# Test using the lower() method

animal = 'BADGER'

print("\nIs the animal a badger?")
print(animal == 'badger')

print("Okay, what about...now?")
print(animal.lower() == 'badger')

# Numerical tests involving equality and inequality,

answer = 30

# greater than, one true one false. 

print("Guess the number!\n")
print("Is the answer greater than 10?")
print(answer > 10)
print("I see, is the answer greater than 40?")
print(answer > 40)

# less than, one true one false
print("\nIs the answer less than 20?")
print(answer < 20)
print("I see, is the answer less than 40?")
print(answer < 40)

# greater than or equal to, one true one false

print("\nIs the answer greater than 25?")
print(answer >= 25)
print("I see, is the the answer greater than 38?")
print(answer >= 38)

# less than or equal to

print("\nIs the answer less than 32?")
print(answer <= 32)
print("I see, is the the answer less than 31?")
print(answer <= 30)

print("\nIs the answer 30?")
print(answer == 30)

print("\nI knew it! And not because I wrote the answer variable either, definitely not.")


# Test using the AND keyword 

answer_2 = 15
answer_3 = 14

print("\nOkay, but can you guess two answers at the same time?!")

print("\nEASY. Are either answers greater than 15?")
# print(answer_2 >= answer) - this works but not directed by exercise 
print(answer_2 > 15 and answer_3 > 15)

print("\nAre both answers less than the ORIGINAL answer?")
print(answer_2 < answer and answer_3 < answer)


# Test using the OR keyword, one true one false

print("\nI see, is either answer less or equal to 10?")
print(answer_2 <= 10 or answer_3 <= 10)

print("\nI see, is either answer less than or equal to 20?")
print(answer_2 <= 20 or answer_3 <= 20)

print("\nAre either answers greater than the ORIGINAL answer?")
print((answer_2 > answer or answer_3 > answer))

print("\nI give up.")

# Test whether an item is in a list
print("\nTesting whether or not a dog is in a list of mine.")

dogs = ['pitbull', 'labrador']
dog = 'pitbull'

if dog in dogs:
    print(f"\nYes, I do like {dog.title()}s!")


# Test whether an item is not in a list
print("\nTesting whether or not a dog is in a list of mine.")

dogs = ['pitbull', 'labrador']
dog = 'chihuahua'

if dog not in dogs:
    print(f"\nNo, I do not like {dog.title()}s!")
