# Classes

Object-oriented programming is one of the most effective approaches to writing software. 
In oop you write **classes** that represent real-world things and situations, and you create 
**objects** based on these classes. 

When you write a class, you define the general behavior that a whole category of objects
can have. When you create individual objects from the class, each object is automatically
equipped with the general behavior; you can give each object whatever unique traits needed.

Making an object from a class is called **instantiation**, and you work with **instances** of 
a class. 

In this chapter you'll write classes and create instances of those classes. 
You'll specify the kind of information that can be stored in instances, and you'll define 
actions that can be taken with these instances. 

You'll also write classes that extend the 
functionality of existing classes, so similar classes can share code efficiently. 


## Definitions 

* Class - a user-defined blueprint or prototype from which objects are created.
Classes can be thought of as categories, they provide a means of bundling data and behaviors. 
Creating a new class creates a new type of object, allowing new instances of that type to be made. 

* Object - an instance of a class. Where the class is the blueprint, an instance is a copy of the class
with actual values. It's not an idea anymore, it's actual data. It's a 2 year old green alien, it's a 6 year old dog.

* Method - a function that's part of a class. 

* Attribute - a variable defined inside of a function | self.thisvariable

* Instance - When you make an object from a class | xyz = Class.whatever