# Overview of Chapter 4

## Working with Lists 

* Using a for loop to cycle through each item in a list until exhausted: 
    * Define a list
    * Define a for loop with a variable
    * Call / utilize variable
    * Each loop replaces the variable with the next item from the list.
    * Every indented line following the for line is inside the loop and will be performed each time.

---
</br>

* Define a for loop with a variable, call via print method</br>

> itemslist = "'item1', 'item2', 'item3',"</br>
>for item in itemslist:</br>
>>print(item)</br>
>
> **additional formatting:**</br>
>> print(f"{item.title()}, found in inventory")</br>
>
> **output**: Item1 found in inventory *(repeated for each item)*

## Lists of numbers 

* `range()` allows manipulation of list output by specifying range of indices to include.</br>

* range will always start counting at the first value provided, and stops when it reaches the second value provided. Because it stops at the second value, it will never contain the end value, in the first line below, 5.

>range(1, 5)</br>
>range(6)</br>

* `range()` also accepts an argument for step size, how many numbers to include in the result. First and second arguments, first and last number to include. 
  
>even_numbers = list(range(2, 11, 2))</br>

**Result:** 
> [2, 4, 6, 8, 10]

See [Even Numbers ](../exercises/even_numbers.py) and [Squares](../exercises/squares.py) exercises for a breakdown.

## Helpful Python functions for numbers

>digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]</br>

**retrieve lowest number:** `min(digits)`</br>
**retrieve highest number:** `max(digits)`</br>
**retrieve sum of all numbers:** `sum(digits)`

## List Comprehensions 

* Comprehensions allow for succinct writing by condensing multiple lines of code to loop through a range and assign to a list into one line of code.

>squares = [value**2 for value in range(1,11)]</br>
>print(squares)</br>

**is equivalent to:**</br> 

>squares = []</br>
>for value in range(1, 11):</br>
>>square = value ** 2</br>
>>squares.append(square)</br>
>
>print(squares)</br>

## Working with Part of a List

* In Python, working with a specific group of items in a list is known as a slice. 

* A slice is made by specifying the index of the first and last elements being worked with. As with the range() function, Python stops one item before teh second index specified. To output the first three elements in a list, specify indices 0 through 3, which would return elements 0,1, and 2.

>players = ['charles', 'martina', 'michael', 'florence', 'eli']</br>
>print(players[0:3])</br>

* Omitting the first index in a slice starts the slice at the beginning of the list. 

>print(players[:4])

## Looping Through a Slice

* A slice can be used in a for loop to loop through a subset of the elements in a list. 


See [Players](../exercises/players.py) exercise for slice examples.

* Some example use cases of Slice: </br>
  * Getting a player's top three scores by sorting the list in decreasing order and taking a slice including just the first three scores.
  * Slicing data into chunks of a specific size.
  * Using slices to display information in a series of pages with an appropriate amount of information on each page in a web application.

## Copying a List

* To copy a list, make a slice that includes the entire original list by omitting the first index and the second index `[:]`. This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list, as shown in [Foods](../exercises/foods.py).

## Tuples 

* Sometimes it will be necessary to create a list of items that cannot change. Tuples allow for that. Python refers to values that cannot change as **immutable**, an immutable list is called a tuple.

## Looping Through All Values in a Tuple

* Tuples can be looped through via a for loop in the same way as lists. 

## Writing over a Tuple

* While tuples cannot be modified directly, a new value can be assigned to a variable that represents a tuple. 

* See examples of these overviews in [Tuples](../exercises/tuples.py) and [Overwrite Tuple](../exercises/overwrite_tuple.py)

## Formatting Guidelines

### Indentation 

* The [PEP8](https://peps.python.org/pep-0008/) style guide for Python recommends using 4 spaces per indentation level. Every text editor provides a setting that lets you use the TAB key but then converts each tab to a set number of spaces. 

### Line Length 

* The PEP8 style guide advises to limit all lines to a maximum of 79 characters. For flowing long blocks of text with fewer structural restrictions, the line length should be limited to 72 characters. 

### Blank Lines 

* To group parts of the program visually, use blank lines within reason. By following the examples in this book the balance should be clear, generally separating lines of code that do different things from one another, defining a list versus accessing data from a list, with one blank line in between.