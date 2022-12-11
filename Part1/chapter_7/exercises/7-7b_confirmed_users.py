'''
Using awhile Loop with Lists and Dictionaries 

A for loop is effective for looping through a list but you shouldn't modify a list 
inside a for loop because Python will have trouble keeping track of items on the list.

To modify a list as you work through it, use a while loop.
Using while loops with lists and dictionaries allows you to collect, store, and 
organize lots of input to examine and report on later.

Consider a list of newly registered but unverified users of a website. 
After verifying the users, how can we move them to a separate list of confirmed
users? One way would be to use a while loop to pull users from the list of  
unconfirmed users as we verify them adn then add them to a separate list of 
confirmed users. 

'''

# Start with the users that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until unconfirmed user list is exhausted.
# Move each verified user into the confirmed list. 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users. 
print("\nThe following users have been verified: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# From previous chapters, we learned the pop() function removes the end
# value and stores it temporarily for transport somewhere else.