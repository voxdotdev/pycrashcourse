# In programming, whitespace refers to any non printing character
# This can include spaces, tabs, and end of line symbols.
# You can use whitespace to organize your output for accessibility 

# Add a tab to your string output via \t

print("\tPython")

# Add a newline in a string via \n 

print("Languages:\nPython\nC\nJavaScript\n")

# Combine tabs and newlines in a single string. 

print("Languages:\n\tPython\n\tC\n\tJavaScript\n")


# Stripping whitespace is important when storing and comparing data
# To a program, 'python' and 'python ' are two different strings

favorite_language = 'python '
print(f"Number of characters with whitespace: {len(favorite_language)}")
favorite_language = 'python'
print(f"Number of characters without whitespace: {len(favorite_language)}")

# An example use case, comparing a username when someone logs onto a website.

# TEMPORARY whitespace stripping is accomplished via the rstrip() method

favorite_language = 'python '

print(f"Number of characters using rstrip temporarily: {len(favorite_language.rstrip())}")
print(f"Calling the variable again you can see it's returned to original. {len(favorite_language)}\n")
# To remove the whitespace permanently
# you have to associate the stripped value with the variable name. 
# meaning strip it as it's assigned to the variable

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(f"Number of characters using rstrip in variable: {len(favorite_language)}")

# To strip whitespace from the left of the string, use lstrip.

favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print(f"Number of characters using lstrip in variable: {len(favorite_language)}")

# or use both
# To strip whitespace from the left of the string, use lstrip.

favorite_language = ' python '
favorite_language = favorite_language.lstrip().rstrip()
print(f"Number of characters using lstrip and rstrip in variable: {len(favorite_language)}")