'''
Write a separate Privileges class. 

The class should have one attribute, privileges, that stores a list 
of strings as described in Exercise 9-7. 

Move the show_privileges() method to this class. 

Make a Privileges instance as an attribute in the Admin class. 

Create a new instance of Admin and user your method to show its privileges.

'''

class User:
    """ User profile information """

    def __init__(self, username, name, location):
        self.username = username
        self.name = name
        self.location = location

    def describe_user(self):
        print(f"The following user has logged on: \
{self.username} | Name: {self.name} | Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello, {self.username}, welcome back.")

class Privileges:
    """ Set privileges for admin users. """
    def __init__(self):
        """Initialization of attributes for Privileges class. """

        self.privileges = ['can add post','can delete post',
        'can ban user','can verify user', 'can promote others']

    def show_privileges(self):
        """ Return list of privileges, neatly formatted. """        
        print(f"List of privileges for Admin: ")
        for priv in self.privileges:
            print(priv.title())

class Admin(User):
    
    def __init__(self, username, name, location):
        """ 
        Initialize Admin class, inheriting from User class. 
        The initialize attribute for privileges from Priv class.
        """
        super().__init__(username, name, location)
        self.granted_privileges = Privileges()


user = Admin('JoeMamma', 'Joe', 'Forks')
user.describe_user()
user.greet_user()
user.granted_privileges.show_privileges()