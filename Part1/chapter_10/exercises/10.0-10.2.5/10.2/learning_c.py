"""
You can use the replace() method to replace a any word in a string 
with a different word. 

message = "I really like dogs." 
message.replace('dog','cat')
'I really like cats'

Read in each line from the file you just created, learning_python.txt, 
and replace the word Python with the name of another language, such as C. 

Print each modified line to the screen. 

"""

filename = 'learning_python.txt'

with open(filename) as file_object:
    data = file_object.readlines()
    
for line in data:
    line = line.replace('Python', 'C')
    print(line.strip())

    