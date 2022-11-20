from user import User

class Privileges:
    """ Set privileges for admin users. """
    def __init__(self):
        """Initialization of attributes for Privileges class. """

        self.privileges = ['can add post','can delete post',
        'can ban user','can verify user', 'can promote others']

    def show_privileges(self):
        """ Return list of privileges, neatly formatted. """
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
        print(f"List of privileges for Admin {self.username}:")