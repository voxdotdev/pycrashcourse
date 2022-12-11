'''
1) Use the code from 6-0f Favorite languages . 

2) Make a list of people who should take the fav languages poll.
Include some names that already exist, and some that do not.

3) Loop through the list of people who should take the poll.
If they have already taken the poll, print a message thanking them for responding.
If they have not taken the poll, print a message inviting them to take the poll. 

'''
#1
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#2 

pollees = ['jen', 'lopez', 'phil', 'collins', 'sarah', 'marshall']

#3

for person in pollees:
    if person in favorite_languages.keys():
        print(f"You've already taken the poll, {person.title()}, thank you!")
    else: 
        print(f"You haven't taken the poll yet, {person.title()}, please do!")

