'''
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 
by replacing your series of print() calls with a loop that runs throught the dictionsary's keys and values. 

When you're sure the loop works, add 5 more Python terms to your glossary. 
When you run the program again, these new words and meanings should automatically be included in the output.
'''


# Internal note: I already wrote 6-3 with a loop, so I expanded the challenge to add glossary terms to the dictionary via user input.
counter = 0

py_glossary = {
    'list':'store information in an ordered group. Lists are similar to arrays in other languages.',
    'loops':'reiterations through a block of code until a condition is fulfilled or met.',
    'functions':'shared with other languages, functions are black boxes, code of an action you might need to repeat often.',
    'parameters':'often shortened to params, these are the variables a function will accept and use.',
    'arguments':'often shortened to args, these are the definitions for params and passed to a function.'
}

print("\nCurrent terms in the glossary: ")
for old_terms in py_glossary.keys():
    print(old_terms.title())


print("\nAdd 5 terms to the glossary!")

for new_term in range(5):
    counter += 1
    term = input(f"Term {counter}:")
    define = input("Define: ")

    py_glossary[term] = define

for key, value in py_glossary.items():
    print(f"\nTerm: {key.capitalize()}")
    print(f"\tDefinition: {value.capitalize()}")

