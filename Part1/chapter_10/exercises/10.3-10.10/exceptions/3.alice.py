"""
Handling the FileNotFoundError Exception 

Let's try to read a file that doesn't exist.
"""

# filename = 'alice.txt'

# with open(filename, encoding='utf-8') as f:
#     contents = f.read()

"""
OUTPUT

Traceback (most recent call last):
  File "d:\2022REPOS\.....\3.alice.py", line 9, in <module>
    with open(filename, encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
"""

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

