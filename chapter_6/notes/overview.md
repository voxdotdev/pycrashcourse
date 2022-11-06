# Overview of Chapter 6

## Dictionaries

This chapter will review how to use Python's dictionaries, which connect pieces of related information, how to access information once it's in a dictionary, and how to modify that information.

Because dictionaries can store an almost limitless amount of information, looping through the data will be explained. Additionally, nesting dictionaries inside lists, lists inside dictionaries, and even dictionaries inside other dictionaries. 

Understanding dictionaries makes it easier to model a variety of real-world objects more accurately, using a dictionary to represent a person and storing as much information as you want about that person.

### [A Simple Dictionary](../exercises/6a_alien.py)

> item_0 = {'color': 'red', 'size': 'medium'}

## Working with Dictionaries

A dictionary in Python is a collection of *key-value pairs*. Each *key* is connected to a value, and a key can be used to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary. 

In Python, a dictionary is wrapped in braces, {}, with a series of key value pairs inside the braces. A *key-value pair* is a set of values associated with each other. When you provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. 

The simplest dictionary has exactly one key-value pair. 

### [Accessing Values in a Dictionary](../exercises/6b_alien.py)

To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets.

### Removing Key-Value Pairs

When you no longer need a piece of information that's stored in a dictionary, 
use the del statement to completely remove a key-value pair. 