class User:
    """ User profile information """

    def __init__(self, username, name, location):
        self.username = username
        self.name = name
        self.location = location

    def describe_user(self):
        print(f"The following user has logged on: \
{self.username} | Name: {self.name} | Location: {self.location}")