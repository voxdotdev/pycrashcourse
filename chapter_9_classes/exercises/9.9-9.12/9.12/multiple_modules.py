"""
Store the User class in one module.
Store the Privileges and Admin classes in a separate module. 

In a separate file (this one), create an Admin instance and call show_privileges()
to show that everything is still working correctly.

"""
from privs_admin import Admin

user = Admin('JoeMamma', 'Joe', 'Arkansas')
user.granted_privileges.show_privileges()

