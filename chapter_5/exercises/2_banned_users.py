# Checking whether a value is not in a list 

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Output - Marie, you can post a response if you wish.

# alternatively, omitting not keyword will require value to be present in list.