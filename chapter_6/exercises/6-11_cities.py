'''
Make a dictionary called cities. 
Use the names of three cities as keys in your dictionary. 

Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact
about that city. 

The keys for each city's dictionary should be something like country, population, and fact. 

Print the name of each city and all of the information you have stored about it


'''

cities = {
    'austin': {'country': 'usa', 'population': '960K', 'fact': 'state: texas'},
    'san francisco': {'country': 'usa', 'population': '820K', 'fact': 'state: texas'},
    'new york': {'country': 'usa', 'population': '8.8M', 'fact': 'state: new york'},
}

for city, city_info in cities.items():
    print(f"\n City: {city.title()}")
    access_info = f"Country: {city_info['country']} Population: {city_info['population']} State: {city_info['fact']}"
    print(access_info.title())