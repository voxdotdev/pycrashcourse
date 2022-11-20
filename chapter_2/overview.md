# Overview of Chapter 2

## Strings
* A string is a series of characters.
* Anything in quotations is considered a string in Python.
* You can use single or double quotes around your strings
  * This allows you to use quotes and apostrophes within your strings

## Creating and printing variables 

* Variable names can contain only letters, numbers, and underscores.
* They can start with a letter or an underscore, but not with a number. 
* Spaces are not allowed in variable names, but underscores can be used to separate words in variable names.
* Avoid using Python keywords and function names as variable names 

</br>

* Values can be assigned to more than one variable using a single line. </br>
`x, y, z = 0, 0, 0`

* Create a variable and store a string</br> 
`message = "texthere"`
* Print a variable storing a string</br>
`print(message)`

* Constants are variables who's values never change, noted by CAPS</br>
`MAX_CONNECTIONS = 3000`

* Comments are internal notes and begin with a hash before each line</br>
`# This is a comment`

## Manipulating strings with Methods

* Convert a string to sentence case</br>
`name = "alice"`</br>
`print(name.title())`

* Convert a string to upper case</br>
`print(name.upper())`

* Convert a string to lower case</br>
`print(name.lower())`

* [List of additional string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## Using variables in strings via F-strings

* F-strings, formally format(), for using a variable inside of a string</br>
`first_name = "alice"`</br>
`print(f"{first_name} is great!")`

* Joining multiple variables inside an f-string, combined with a string method</br>
`first_name = "alice"`</br>
`last_name = "wonderland"`</br>
`full_name = f"{first_name} {last_name}"`</br>
`message = f"Hello, {full_name.title()}!"`</br>
`print(message)`

## Adding and removing whitespace to / from Strings

* Temporarily remove extra spaces from a variable</br>
`favorite_language = 'python '`</br>
`print(favorite_language.rstrip())`</br>

* Permanently remove whitespace from a variable</br>
`favorite_language = 'python '`</br>
`favorite_language = favorite_language.strip()`</br>

* Strip right whitespace only</br>
`favorite_language.rstrip()`

* Strip left whitespace only</br>
`favorite_language.lstrip()`

## Numbers

* Any number with a decimal point is referred to as a float.

* Dividing any two numbers, even if they are integers that result in a whole number, will always produce a float.

* Long numbers can be grouped up using underscores to make large numbers more readable. Printing these only prints the digits.