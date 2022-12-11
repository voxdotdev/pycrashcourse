''''
Add an attribute called login_attempts to your user class from 
exercise 9-3. [x]

Write a method called increment_login_attempts() that increments the 
value of login_attempts by 1. [x]

Write another method called reset_login_attempts() that resets the value 
of login_attempts to 0. [x]

Make an instance of the User class and call increment_login_attempts()
several times. 

Print the value of login_attempts to make sure it was incremented properly,
and then call reset_login_attempts().

Print login_attempts again to make sure it was reset to 0.  

'''


class User:
    """ User profile information """

    def __init__(self, username, name, location):
        self.username = username
        self.name = name
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """ Return a neatly formatted descriptive name """
        long_name = f"{self.username} {self.name} {self.location}"
        return long_name

    def greet_user(self):
        greeting = f"Welcome back, {self.name.title()}"
        return greeting

    def read_login_attempts(self):
        """ Print amount of login attempts """
        print(f"Login attempts: {self.login_attempts}")

    def increment_login_attempts(self, attempt_number):
        """ Add the given amount to the number of login attempts. """
        self.login_attempts += attempt_number
   
    def reset_login_attempts(self):
        self.login_attempts -= self.login_attempts
        print("Login attempts reset!")
        
    
login = User('fearlesspenguin', 'angie', 'los angeles')
print(login.describe_user, login.greet_user)
login.increment_login_attempts(1)
login.read_login_attempts()

login = User('thelegend27', 'mark', 'seattle')
login.increment_login_attempts(2)
login.read_login_attempts()

login = User('mystic', 'joani', 'juniper')
login.increment_login_attempts(3)
login.read_login_attempts()

login.read_login_attempts()
login.reset_login_attempts()

# later on this could be a for loop for each user input, wait for user input.
# overall this is terrible code, increment for user login count should obviously not be coming from user / input 
# but should increment automatically. This is just for the sake of explanation.