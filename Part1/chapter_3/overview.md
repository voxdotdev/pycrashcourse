# Overview of Chapter 3

## Lists

* A list is a collection of items in a particular order. Anything can be put into a list, and the items in the list do not have to be related in any particular way.

* Like most programming languages, Python considers the first item in a list to be at position 0, not position 1. 

## Creating and Accessing Lists 

* Create a list</br>
`list = ['item0', 'item1', 'item2']`

* Create an empty list</br>
`list = []`

* Print a list</br>
`print(list)`

* Access an item in a list</br>
`print(list[0])`

* Access and format output of a list with string methods</br>
`print(list[0].title())`

* The position [-1] refers to the last item in a list</br>
`print(list[-1])`

* The position [-2] refers to the second to last item, and so on</br>
`print(list[-2])`

## Modifying Lists

* Change an item in a list by referencing it's position in the list</br>
`list[0] = 'newitem'`

* Add an item to the end of a list</br>
`list.append('item')`

* Insert a new value into a list</br>
`list.insert(0, 'item')`

* Delete an item from a list by referencing position</br>
`del list[0]`

* Remove and reuse the last item from a list</br>
`popped_item = list.pop()`

* Remove and reuse any item from a list by referencing position</br>
`popped_item = list.pop(2)`

* Remove and item from a list</br>
`list.remove('item')`

* Remove and reuse an item from a list</br>
`list = ['item0', 'item1', 'item2']`</br>
`stored_item = 'item1'`</br>
`list.remove(stored_item)`

## Organizing Lists

Sorting a list permanently changes its order.

* Sort a list alphabetically</br>
`list = ['item0', 'item1', 'item2', 'item3']`</br>
`list.sort()`

* Sort a list alphabetically backwards</br>
`list = ['item0', 'item1', 'item2', 'item3']`</br>
`list.sort(reverse=True)`

* Another method of sorting backwards</br>
`list = ['item0', 'item1', 'item2', 'item3']`</br>
`list.reverse()`

* Temporarily sort a list </br>
`print(sorted(list))`

* Find the length of a list</br>
`list = ['item0', 'item1', 'item2', 'item3']`</br>
`len (list)`</br>
`print(len(list))`

## Avoiding Index Errors

* Calling the last item in the list </br>
`list[-1]` 