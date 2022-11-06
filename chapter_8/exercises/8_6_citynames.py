'''
Write a function called city_country() that takes in the name 
of a city and its country. 

The function should return a formatted string like: "Santiago, Chile" 

Call your function with at least three city-country pairs
Print the values that are returned.
'''
destinations = [] # Extra credit adding answers to a list!

def get_formatted_location(city, country):
    full_location = f"{city}, {country}"
    return full_location.title()

while True:
    print("\nWhere would you like to travel to?")
    a_city = input("City: ")
    if a_city == "no":
        break
    a_country = input("Country: ")
    if a_country == 'no':
        break
    formatted_location = get_formatted_location(a_city, a_country)
    destinations.append(formatted_location)
    print(f"\nSo you want to go to {formatted_location}! That's a beautiful place.")

print(f"Here's your bucket list of places to go: {destinations}")