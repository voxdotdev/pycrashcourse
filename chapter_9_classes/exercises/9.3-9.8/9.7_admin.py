'''
An administrator is a special kind of user. 

Write a class called Admin that inherits from the User class you wrote in 
Exercise 9-3 or 9-5. 

Add an attribute, privileges, that stores a list of strings like "can add post",
"can delete post", "can ban user", and so on. 

Write a method called show_privileges() that lists the admin's set of privileges.

Create an instance of Admin, and call your method.

'''

class User:
    """ User profile information """

    def __init__(self, username, name, location):
        self.username = username
        self.name = name
        self.location = location

    def describe_user(self):
        print(f"Username: {self.username} | Name: {self.name} | Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello, {self.username}, hope the weather's nice in {self.location}.")

class Admin(User):
    
    def __init__(self, username, name, location):
        """ Initialize Admin class, inheriting from User class. """

        super().__init__(username, name, location)
        self.privileges = ['can add post','can delete post',
        'can ban user','can verify user', 'can promote others']

    def show_privileges(self):
        
        print(f"List of privileges for user {self.username}: ")
        for priv in self.privileges:
            print(priv.title())


privs = Admin('JoeMamma', 'Joe', 'Joshua Tree')
privs.show_privileges()