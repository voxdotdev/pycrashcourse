""" 
Writing to a File 


Writing to an Empty File 

To write text to a file, you need to call open() with a second argument telling 
Python that you want to write to the file. To see how this works, let's write a 
simple message and store it in a file instead of printing it to the screen: 

"""

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("\nI love creating new games.") # (2)

"""
The second argument, 'w' tells Python we want to open the file in write mode. 

You can open a file in 'r' read mode, 'w' write mode, 'a' append mode, or a 
mode that allows you to read and write to the file ('r+').

If you omit the mode arg Python opens in read-only by default. 

The open function automatically creates the file you're writing to if it doesn't 
already exist. With 'w' however, Python will erase the contents of the file before 
returning the file object. 

We use the write() method to write a string to the file. 
This program has no terminal output, but if you open the file programming.txt, you'll 
see our string. 

(2) Writing multiple lines 

Include a \n to move to the next new line after each sentence. 

"""
