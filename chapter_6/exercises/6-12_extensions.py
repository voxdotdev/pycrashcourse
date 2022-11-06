'''
Extensions: We're now working with examples that are complex enough that they can be extended in any number of ways. 

Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.

*Used values from Amazon's New World 
'''
   
# A Dictionary in a Dictionary 

#string instruments

strings = {
    'green_quantities': {'timber': 10,'iron ingot': 3,'obsidian sandpaper': 4,'ash stain': 15},
    'blue_quantities': {'lumber': 15, 'steel ingot': 4, 'obsidian sandpaper': 5, 'maple stain': 20, 'catfish whiskers': 4},
    'guitar_purple_quantities': {'stone brick': 25,'obsidian flux': 4,'brilliant pearl': 3,'catfish whiskers': 4},
    'mandolin_purple_quantities': {'stone brick': 25,'obsidian flux': 4,'brilliant stone': 3,'catfish whiskers': 4}    
}

for key, value in strings.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Modifying values 
output = 2
calc = (strings['green_quantities']['timber'] * output)

print(f"Amount needed: {calc}")
