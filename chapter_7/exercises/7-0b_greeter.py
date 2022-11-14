'''
Writing Clear Prompts 

Each time you use the input, include a clear, easy to follow prompt for the user. 

'''

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

'''
Sometimes you'll want to write a prompt that's longer than one line. 
To do this you can assign your prompt to a variable and pass that variable to the input function. 

'''

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name1 = input(prompt)

'''
Using int to Accept Numerical Input

By default, Python interprets everything provided by the user as a string. 
To resolve this, use the int function to convert the string to an int.

'''

age = input("How old are you? ")
age = int(age)

age >= 18

