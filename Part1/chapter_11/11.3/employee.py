"""
Write a class called Employee.

The __init__() method should take in a first name, last name, and an annual salary. 
Store each of these as attributes. 

Write a method called give_raise() that adds $5,000 to the annual salary by default 
but also accepts a different raise amount. 

Write a test case for Employee.
Write two test methods, test_give_default_raise() and test_give_custom_raise().

Use the setUp() method so you don't have to create a new employee instance 
in each test method. 

Run your test case, and make sure both tests pass.
"""

class Employee():

    def __init__(self, fname, lname, salary):
        """Store employee information."""
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self, amount=''):
        """Provides a default raise unless a value is given."""
        if amount:
            self.salary += amount
        else:
            self.salary += 5000
