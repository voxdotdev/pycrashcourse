'''
Using a flag 

In a game, several different events can end the game. 
When a player runs out of resources, their time runs out, or entities they were supposed to protect are all destroyed, the game should end.
If many possible events might occur to stop the program, trying to test all these conditions in one while statement becomes complicated. 

For a program that should run only as long as many conditions are true, you can define one variable that determines whether or nto 
the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag 
isi set to True, and stop running when any of several events sets the value of the flag to False. 

As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True. 

'''

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)