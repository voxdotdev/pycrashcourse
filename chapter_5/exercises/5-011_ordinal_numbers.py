"""
5-11. Ordinal Numbers:

Ordinal numbers indicate their position in a list, such as 1st or 2nd. 
Most ordinal numbers end in th, except 1,2, and 3. 

• Store the numbers 1 through 9 in a list 
• Loop through the list 
• Use an if-elif-else chain inside the loop to print the proper ordinal end-ing for each number. 
• Output should read "1st 2nd 3rd 4th and so on up to 9th, each result should be on a separate line. 

"""

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in ordinal_numbers:
    if number < 2:
        print(f"{number}st! \n")
    elif number < 3:
        print(f"{number}nd!\n")
    elif number < 4:
        print(f"{number}rd!\n")
    else:
        print(f"{number}th!\n")