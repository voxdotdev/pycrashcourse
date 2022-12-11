'''
A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion we'll call it a glossary. 

Think of 5 programming words you learned about in the previous chapters.
Use these words as the keys in your glossary and store their 
meanings as values. 

Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print
the word on one line, then print its meaning indented on a second line.

Use the newline character \n to insert a blank line between each word-meaning
pair in your output.

'''

py_glossary = {
    'list':'store information in an ordered group. Lists are similar to arrays in other languages.',
    'loops':'reiterations through a block of code until a condition is fulfilled or met.',
    'functions':'shared with other languages, functions are black boxes, code of an action you might need to repeat often.',
    'parameters':'often shortened to params, these are the variables a function will accept and use.',
    'arguments':'often shortened to args, these are the definitions for params and passed to a function.'
}

for key, value in py_glossary.items():
    print(f"\nTerm: {key.capitalize()}")
    print(f"\tDefinition: {value.capitalize()}")