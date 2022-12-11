"""
Open a blank file in your text editor and write a few lines summarizing
what you've learned about Python so far. Start each line with the phrase
In Python you can...

Save the file as learning_python.txt in the same directory as this exercise.

Write a program that reads the file and prints what you wrote three times. 

Print the contents once by reading the entire file, once by looping over 
the file object, and once by storing the lines in a list, then working with 
them outside the with block. 

"""
filename = 'learning_python.txt'

# Print via reading entire file
print("\nPrint via reading entire file: ")
with open(filename) as file_object:
    data = file_object.read()
    print(data.strip())

# Print via reading line by line 

print("\nPrint via reading line by line: ")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# Print by storing items in list, then printing outside block

print("\nPrint by storing items in list, then printing outside block: ")
with open(filename) as file_object:
    data = file_object.readlines()

for line in data:
    print(line.strip())