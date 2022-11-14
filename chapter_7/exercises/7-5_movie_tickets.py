'''
A movie theater charges different ticket prices depending on a person's age. 

If a person is under the age of 3, the ticket is free. 

If they are between 3 and 12, the ticket is $10. 

If they are over age 12, the ticket is $15. 

Write a loop in which you ask users their age
Then tell them the cost of their move ticket.

'''
prompt = "How old are you? "

age = 0

while age < 13:
    age = input(prompt)
    age = int(age)
    
    if age < 3:
        print(f"\nThe ticket price for age {age} is nothing!")
        break
    elif age <= 12:
        print(f"\nThe ticket price for age {age} is $10.")
        break
    else:
        print(f"The price for age {age} is $15.")