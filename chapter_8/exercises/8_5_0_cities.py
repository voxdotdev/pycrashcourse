"""
Write a function called describe_city() that accepts the name of a city and its country
The function should print a simple sentence such as Reykjavik is in Iceland. 
Give the param for the country a default value
Call the function for three different cities, at least one of which is not in the default country.

"""

def describe_city(city, country='Iceland'):
    print(f"{city} is in {country}.")

describe_city('Reykjavik')
describe_city('New York', country='United States')
describe_city('Havana','Cuba')