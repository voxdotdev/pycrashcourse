'''
Write a program that polls users about their dream vacation.

Write a prompt similar to 'If you could visit one place in the world,
where would you go?'

Include a block of code that prints the results of the poll.

'''

responses = {}

working = True

while working:

    name = input("What is your name? ")
    answer = input("What's your dream vacation, one place in the world you want to go? ")

    responses[name] = responses

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        working = False

print("\n--- Poll Results ---")
for items, response in responses.items():
    print(f"{name.title()} would like to visit {answer.title()}.")