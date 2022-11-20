'''
Make a class called User. 
Create two attributes called first_name and last_name,
then create several other attributes that are typically stored 
in a user profile.

Make a method called describe_user() that prints a summary of the 
user's information. 

Make another method called greet_user() that prints a personalized 
greeting to the user. 

Create several instances representing different users, call both methods for each.
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

user1 = User('fearlesspenguin', 'angie', 'los angeles')
user1.describe_user()
user1.greet_user()
user2 = User('thelegend27', 'mark', 'seattle')
user2.describe_user()
user2.greet_user()
user3 = User('mystic', 'joani', 'juniper')
user3.describe_user()
user3.greet_user()

