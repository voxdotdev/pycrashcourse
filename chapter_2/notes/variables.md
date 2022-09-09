## Variable Rules and Guidelines

* Variable names can contain only letters, numbers, and underscores.
* They can start with a letter or an underscore, but not with a number. 
* Spaces are not allowed in variable names, but underscores can be used to separate words in variable names.
* Avoid using Python keywords and function names as variable names 
  - keywords will error, function names will override that functions behavior
* Variable names should be short but descriptive. Name is better than n, student_name is better than s_n, name_length is better than length_of_persons_name.
* Be careful when using lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.
* Generally, variables should be lowercase, as uppercase letters in variable names have special meanings.

**Valid Variables**

_dog</br>
dog_1</br>
a_dog</br>
small_dog</br>

**Invalid Variables** 

1_dog</br>
small dog

**[Python Keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)**


**[Python Built-in Functions](https://docs.python.org/3/library/functions.html)**


### Multiple Assignment

Values can be assigned to more than one variable using a single line. 

For example: 

> x, y, z = 0, 0, 0

The variable names and values must be separated by commas. Python will assign each value to its respective positioned variable. As long as the number of values matches the number of variables, Python will match them up correctly. 

### Constants

A *constant* is a variable whose value stays the same and will never change. 

Python does not have built-in constant types, but Python programmers use all capital letters to indicate when a variable should be treated as a constant. 

> MAX_CONNECTIONS = 5000

### Comments 

Comments are noted lines to document behaviors and expectations for the written code.
Your future self and others who need to read your code later on will thank you. 

Comments begin with a hash: </br> # Single line comment
