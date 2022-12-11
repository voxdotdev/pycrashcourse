from name_function import get_formatted_name

print("Enter q at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")

    """
    This program imports get_formatted_name() from name_function.py.

    We can see the names are generated correct here, but let's say we want
    to modify get_formatted_name() to accept middle names. 

    As we do so, we want to make sure we don't break the way the function 
    handles names that have only a first and last name. 

    Rather than testing with user input each time, we can automate the testing
    with Unit Tests and Test cases.
    """