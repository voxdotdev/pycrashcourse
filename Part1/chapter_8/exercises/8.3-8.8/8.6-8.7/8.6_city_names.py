'''
Write a function called city_country() that takes 
in the name of a city and its country. The function should return a string 
formatted like: 

"Santiago, Chile" 

Call your function with at least three city-country pairs, 
print the values that are returned.

'''

def city_country(city, country):
    format_location = f"{city}, {country}"
    return format_location.title()


while True: 
    print("\nEnter a city and country you'd like to visit: ")
    print("\n(Or input 'q' to quit)")

    city = input("Enter city: ")
    if city == 'q':
        break
    country = input("Enter country: ")
    if country == 'q':
        break

    formatted_place = city_country(city, country)
    print(f"{formatted_place} sounds lovely!")


"Used user input over specifying values, that's at least 3, if user wants."