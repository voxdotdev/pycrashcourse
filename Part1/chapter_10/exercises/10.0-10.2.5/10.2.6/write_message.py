"""
Appending to a File 

Remember the 3 modes of opening a file; read, write, append. 
r+ as shortcut for read and write.

Any lines you append to a file will be added to the end of the file. 

"""


filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.")
    file_object.write("\nI love creating apps that can run in a browser.")