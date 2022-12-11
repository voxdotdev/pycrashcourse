class Restaurant:
    """ Restaurant details """

    def __init__(self, name, cuisine):
        " Initialize name and cuisine type attributes "
        self.name = name 
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"{self.name} is now open.")

    def hours(self):
        print(f"{self.name} is open M-S 10:00 AM to 8:00 PM.")
