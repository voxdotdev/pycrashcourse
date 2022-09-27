""" 
5-10. Checking Usernames 

Do the following to create program that simulates how websites 
ensure that everyone has a unique username.

• Make a list of five or more usernames called current_users
• Make another list of five usernames called new_users. 
Make sure one or two of the new usernames are also in the current_users list. 
• Loop through the new_users list to see if each new username has already been used. 
• If it has, print a message that the person will need to enter a new username. 
• If a username has not been used, print a message saying that the username is available.
• Make sure the comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
To do this, the current_users list will need to be copied, containing the lowercase versions of all existing users. 


"""

current_users = ['thelegend27','user1','user2','user3','user4']


new_users = ['thelegend27','user1','USER1','user6','user7']


for new in new_users:
    new = new.lower() #instead of copying current_user list, setting new username entry to lowercase. 
    if new in current_users:
        print(f"Sorry, {new} has been taken.")
    else:
        print(f"{new} is available!\n")


""" 
Exercise using user input - not directed by book.
not perfect, just experimenting.

"""

current_users = ['thelegend27','user1','user2','user3','user4']

new_users = []

new_user = input("Enter desired username: ")
new_user = new_user.lower()

if new_user in current_users:
    print(f"Sorry, {new_user} has already been taken.")    
else:
    new_users.append(new_user)
    print(f"{new_user} is available!")
    print(f"list of new usernames registered today: {new_users}")
