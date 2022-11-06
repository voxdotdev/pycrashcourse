##  Difference between List and Dictionary in Python 

Lists are akin to arrays in other languages.
List contents do not need to be related to each other. 

EXAMPLE OF LIST: 

**Creating a List with the use of multiple values**</br>
>List = ["Geeks", "For", "Geeks"]
print("List containing multiple values: ")
print(List[0]) </br>
print(List[2])
   
**Creating a Multi-Dimensional List ()By Nesting a list inside a List)**</br>
>List = [['Geeks', 'For'] , ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

**Output:**

>**List containing multiple values:**</br>
Geeks</br>
Geeks

>**Multi-Dimensional List:**</br>
>[['Geeks', 'For'], ['Geeks']]

Dictionaries are unordered collections of data values , 
used to store data values like a map, which unlike other Data Types that hold only asingle value as an element, Dictionary holds key:value pair. 

Key value is provided in the dictionarty to make it more optimized. 

Each key-value pair in a Dicitonary is separated by a colon:
Whereas each key is separated by a comma, 

EXAMPLE OF DICTIONARY:

**Creating a Dictionary with Integer Keys**</br>

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}</br>
print("Dictionary with the use of Integer Keys: ")</br>
print(Dict)</br>

**Creating a Dictionary with Mixed keys**</br>

>Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}</br>
print("\nDictionary with the use of Mixed Keys: ")</br>
print(Dict)

**Output**

>**Dictionary with the use of Integer Keys:**</br>
{1: 'Geeks', 2: 'For', 3: 'Geeks'}

>**Dictionary with the use of Mixed Keys:**</br>
{1: [1, 2, 3, 4], 'Name': 'Geeks'}