## Numbers

Numbers are used for countless things, to keeping score in games, representing data in visualizations, and so on.

Python treats numbers in several different ways, depending on how they're being used.

Easiest to tackle is how Python manages integers.

### Integers 

* You can add + , subtract - , multiply * and divide / integers in Python
* Exponents are represented with ** 
* Python supports the order of operations

### Floats 

Any number with a decimal point is referred to as a float.
This term is used in most programming languages and refers to the fact that a decimal point can appear to any position in a number. 

For the most part, decimals can be used without worrying about how they behave, although sometimes an arbitrary number of decimal places in your answer / returned value.

> 0.2 + 0.1</br>
0.30000000000000004</br>
3 * 0.1</br>
0.30000000000000004</br>

This can be ignored for now, ways to deal with the extra places will be explained later on.

### Integers and Floats

Dividing any two numbers, even if they are integers that result in a whole number, will always produce a float.

> 4/2</br>
2.0

Mixing an integer and a float in any other operation will a float as well:

> 1 + 2.0</br>
3.0</br>
2 * 3.0</br>
6.0</br>
3.0 ** 2</br>
9.0</br>


### Underscores in Numbers

Long numbers can be grouped up using underscores to make large numbers more readable.

> universe_age = 14_000_000_000

Printing a number with underscores
only prints the digits. Python ignores the underscores when storing these kinds of values. To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature works for integers and floats, but it’s only available in Python 3.6
and later.

> print(universe_age)</br>
14000000000