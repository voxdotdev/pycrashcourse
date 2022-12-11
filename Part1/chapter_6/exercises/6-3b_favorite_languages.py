

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# .items() to include both keys and values

print("The following languages have been mentioned:")
for person, language in favorite_languages.items():
    print(f"{person.title()} likes {language.title()}!")

# .keys() to only include the keys

print("We surveyed the following people:")
for person in favorite_languages.keys():
    print(person.title())

# .values() to only include values

print("These are the languages people preferred:")
for langs in favorite_languages.values():
    print(langs.title())

# .if statement to check if a key, or a value, by swapping the function used as explained above, exists in a dictionary.
friends = ['phil', 'sarah']
for person in favorite_languages.keys():
    print(person.title())

    if person in friends:
        language = favorite_languages[person].title()
        print(f"\t{person.title()}, I see you love {language}!")