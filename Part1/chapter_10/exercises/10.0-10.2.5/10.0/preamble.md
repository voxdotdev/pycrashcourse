
## Chapter 10 

In this chapter you'll learn to work with files so your programs 
can quickly analyze lots of data. 

You'll learn to handle errors so your programs don't crash when they
encounter unexpected situations. 

You'll learn about EXCEPTIONS, which are special objects Python creates 
to manage errors that arise while a program is running. 

You'll also learn about the json module, which allows you to save user data
so it isn't lost when your program stops running. 

### Reading from a File 

An incredible amount of data is available in text files. 
Text files can contain weather data, traffic data, socioeconomic data, literary works,
and more. Reading from a file is particularly useful in data analysis applications.

When you want to work with the information in a text file, the first step is to read 
the file into memory. You can read the entire contents of a file or you can work 
through the file one line at a time.

#### Reading an Entire File 

To begin we need a file with a few lines of text in it. 
We'll start with pi_digits.txt that contains pi to 30 decimal places
with 10 decimal places per line.