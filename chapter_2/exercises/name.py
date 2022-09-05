# The method title() appears after the variable in the print call. 
# A method is an action that Python can perform on a piece of data. 
# The . after name tells Python to make the title method act on the variable NAME
# Every method is followed by a set of parentheses.
# The title function doesn't need any additional information, so its parentheses are empty.

# The title method changes each word to title case, where each word begins with a capital letter.
# This is useful for when you want your program to treat ADA ada and Ada as the same name, 
# and display all of them as Ada.

name = "ada lovelace"
print(name.title())


# The examples below convert the string to upper and lower case, respectively.

name = "Ada Lovelace"
print(name.upper())

# This lower method is particularly useful for storing data.
# If storing input, convert to lowercase.
# If displaying stored data to user, convert using a suitable method.

name = "Ada Lovelace"
print(name.lower())