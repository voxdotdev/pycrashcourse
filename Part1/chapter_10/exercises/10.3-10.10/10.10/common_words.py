"""
Visit Project Gutenberg (gutenberg.org) and find a few texts you'd like to analyze.

Download the text files for these works, or copy the raw text from your browser into a
text file on your computer.

You can use the count() method to find out how many times a word or phrase appears in
a string, using the lower() function to convert all to lower case to match case. 

line = "Row, row, row your boat"
line.lower().count('row')


"""
def count_words(filename):
    """ Count the approximate number of words in a file. """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        keyword = 'shall'
        num_words = words.count(keyword)
        print(f"The file {filename} uses the word '{keyword}' about {num_words} times.")



filename = 'dorian_gray.txt'
count_words(filename)
