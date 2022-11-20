"""
Start with your work from Exercise 9-8. 

Store the classes User, Privileges, and Admin in one module. 

Create a separate file, make an Admin instance. 

Call show_privileges to show that everything is working correctly.
"""

from privileges import Admin

user = Admin('JoeMamma', 'Joe', 'Arkansas')
user.granted_privileges.show_privileges()

