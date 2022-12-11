'''Modify your program from Exercise 6-2 so each person can have more than one favorite number. 

Then print each person's name along with their favorite numbers.

'''

friendfav_numbers = {
    'alan': ['1','2','3'],
    'albert': ['4','5','6'],
    'alison': ['7','8','9'],
    'alice': ['10','11','12'],
    'alicia': ['13','14','15'],
}

for person, number in friendfav_numbers.items():
    print(f"\n{person.title()}")
    print("Favorite numbers:")
    for numbers in number:
        print(f"{numbers}")