""" Reading an Entire File """

with open('pi_digit.txt') as file_object:
    contents = file_object.read()
print(contents)


"""
To do any work with a file, even just printing its contents, you first need to 
open the file to access it. The open() function needs one argument: the name of the 
file you're trying to open. Python looks for this file in the same directory the 
program is being executed from.

The keyword 'with' closes the file once access to it is no longer needed. 
You could close the program with close(), but if a bug in your program prevents 
the close() method from being executed, the file may never close. It's also not always
easy to tell exactly when to close a file. 


Once we have the file object representing the text file, we use the read() method to
read the entire contents of the file and store it as one long string in 'contents'. 
Thus, when we print the value of contents, we get the file text back. 

The only difference between the file and our output is the extra blank line at the end 
of the output. This appears because read() returns an empty string when it reaches the 
end of a file. If you want to remove the extra blank lin, you can use rstrip() in the 
call to print().

File Paths: 
To look outside of the current directory, you need to provide the file path. 

Relative file path - tells Python to look for a given location relative 
to the directory where the currently running program file is stored. 

with open('somesubdir/pi_digit.txt') as file_object:
    contents = file_object.read()
print(contents)

Absolute file path - tells Python exactly where the file is on the computer,
regardless of where the program that's being executed is stored.

file_path = '/somerootdir/Auser/other_files/text_files/pi_digit.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)


If you try to use backslashes in a file path you'll get an error because the 
backslash is used to escape characters in strings, like \t for tab.

"""

