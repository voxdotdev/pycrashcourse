"""
Modify the function from 11.1 so it requires a third parameter, population.

It should now return a single string of the form City, Country - population xxx,
such as Santiago, Chile - population 5000000. 

Run test_cities.py again, Make sure test_city_country() fails this time.
(skipping, we know how to make it fail, by requiring population vs optional.)

Modify the function so the population parameter is optional. 
Run test_cities.py again, make sure test_city_country() passes again.

Write a second test called test_city_country_population() that verifies you
can call your function with the values 'santiago', 'chile', and 'population=5000000'.

Run test_cities.py again, and make sure this new test passes. 
"""

"""A collection of functions for working with cities."""

def city_country(city, country):
    """Return a string representing a city-country pair."""

    output_string = f"{city.title()}, {country.title()}"
    return output_string
