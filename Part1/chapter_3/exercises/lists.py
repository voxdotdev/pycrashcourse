# Exercises


## 3-1. Names 
### Store the names of a few of your friends in a list called names 
### Print each person's name by accessing each element in the list, one at a time.

names = ['alice', 'adam', 'amy','alex']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

## 3-2. Greetings
### Start with the list used in exercise 3.1, but instead of just printing 
### each name, print a message to them. The text of each message should be the same, 
### but each message should be personalized with the person's name. 

message = f"Hello, {names[0].title()}."
print(message)

message = f"Hello, {names[1].title()}."
print(message)

message = f"Hello, {names[2].title()}."
print(message)

message = f"Hello, {names[3].title()}."
print(message)

## 3-3. Your Own List: 
### Think of your favorite mode of transportation, such as a motorcycle or a car.
### Make a list that stores several examples.
### Use your list to print a series of statements about these items, such as 
### "I would like to own a Honda motorcycle."

transport = ['coop', 'vw bus', 'a clown car']
opinion = f"nothing is cuter than a {transport[0].title()}"
print (opinion)

opinion2 = f"nothing is cooler than a {transport[1].title()}"
print (opinion2)

opinion3 = f"nothing is sillier than a {transport[2].title()}"
print (opinion3)


