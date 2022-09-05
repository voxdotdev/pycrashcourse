# In some situations you'll want to use a variable's value inside a string.
# You might want two variables to represent a first name and a last name,
# and then combine those values to display a full name: 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# To insert a variable's value into a string: 
# Place the letter f immediately before the opening quotation mark.
# Put braces around the name or names of any variable you want to use inside.
# These strings are called f-strings. F being for format.
# Python formats the string by replacing the name of any variable in braces.

# More examples using f-strings

## Applying a method to the combined variable

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())

## Wrapping an f-string around our f-string variable

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name}!")

## Same as above but converting output to sentence casing via title().

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# It is also possible to assign a f-string to a variable, as shown below
# This makes things cleaner, and calling the final print() function easier.

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# Note: Python 3.5 and earlier uses fortmat() rather than this f syntax
# Syntax: full_name = "{} {}".format(first_name, last_name)