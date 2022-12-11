# 3-4 Guest List 
## Make a list that includes at least three people you'd like to invite to dinner. 
## Then, use the list to print a message to each person, inviting them to dinner.

guests = ['J.Neutron', 'L.Lohan','P.Stewart','Yogi']

print(f"Dear {guests[0]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[1]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[2]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[3]}, you are cordially invited to some dinner party for some reason.")

# 3-5 Changing Guest List 
## Start with the program from 3-4.

guests = ['J.Neutron', 'L.Lohan','P.Stewart','Spock']

## Modify the list, replacing the name of the guest who can't make it 

uninvited_guest = guests.pop(1)

## with the name of the new person being invited 
guests.append('A.Lincoln')


## Print a second set of invitation messages, one for each person who is still in your list. 

print(f"Dear {guests[0]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[1]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[2]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[3]}, you are cordially invited to some dinner party for some reason.")

## Add a print() call at the end of the program stating the name of the guest who can't make it.

print(f"Shout out to {uninvited_guest} who couldn't make it.")

## 3-6 More Guests
# Start with the program from 3-5.
guests = ['J.Neutron', 'A.Lincoln','P.Stewart','Spock']

# Add a print call to the end of the program announcing a bigger dining table has been found.

print("A bigger table has been found, meaning more room for people!")

# Use insert() to add one new guest to the beginning of the list

guests.insert(0, 'Mom')

# Use insert() to add one new guest to the middle of the list 

guests.insert(2, 'Madonna')

# Use append() to add one new guest to the end of the list 

guests.append('A. St. Bernard')
# Print a new set of invitation messages, one for each person. 

print(f"Dear {guests[0]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[1]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[2]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[3]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[4]}, you are cordially invited to some dinner party for some reason.")
print(f"Dear {guests[5]}, you are cordially invited to some dinner party for some reason.")

# 3-9 Dinner Guests 
# Working with one of the programs from Exercise 3-4
# use len() to print a message indicating the number 
# of people you are inviting to dinner

print(f"There are now {len(guests)} attendees.")
