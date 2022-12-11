# Exercises to avoid syntax errors when including apostrophes in strings. 

## 2-3 Personal message

# Use a variable to represent a person's name

name = "george"

# Print a simple message to that person using an apostrophe.

message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

# output: Hello George, would you like to learn some Python today?

## 2-4 Name Cases

# Use a variable to represents person's name

name = "george"

# Print that person's name in lowercase, uppercase, and title case

print(f"...{name.lower()}. {name.upper()}! {name.title()}.\n")

# output: ...george. GEORGE! George.

## 2-5 Famous Quote

# Find a quote from a famous person you admire
# Print the quote and the name of its author. 
# Output should contain quotation marks and at least 1 apostrophe

print('"Use the force, Harry!"\n - Gandolf, Captain of the starship Enterprise\n')

## 2-6 Famous Quote 2

# Repeat exercise 2-5 but this time represent the person's name using a variable famous_person

famous_person = "Gandolf, Captain of the starship Enterprise"

# Compose message and represent it with a new variable called message. Print. 

message = '"Use the force, Harry!"'
print(f'{message}\n - {famous_person}\n')

## 2-7 Stripping Names

# Use a variable to represent a person's name 
# Include some whitespace characters at the beginning and end of the name. 

persons_name = " rolf "

# Print the name once, so the whitespace around the name is displayed.

print(persons_name) 

# Then, print the name using each of the three stripping functions.

# Print using lstrip())

persons_name = persons_name.lstrip()
print(persons_name)

# Print using rstrip()

persons_name = persons_name.rstrip()
print(persons_name)

# Print using strip()

persons_name = persons_name.strip()

# # Make sure to use each character combination, "\t" and "\n" at least once
print(f"\t{persons_name}\n")