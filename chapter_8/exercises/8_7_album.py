'''
1) Write a function called make_album() that builds a dictionary 
describing a music album. 

The function should take in an artist name and an album title.
2) It should return a dictionary containing these two pieces of information.

3) Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album info correctly.

Use None to add an option parameter to make_album() that allows you to 
store the number of songs on an album. 

If the calling line includes a value for the number of songs
add that value to the album's dictionary.

Make at least one new function call that includes the number of songs on an album.
'''

# 1 - 3
def make_album(name, album, songs='none'):
    ''' Return the arists and albums as a dictionary. '''
    release = {'artist': name, 'album': album, 'tracks': songs}
    return release

print("Enter 3 artist releases!")
for entry in range(3):
    musician = make_album(input("Enter Artist: "), input("Enter Album: "), input("How many songs have you listened to? "))
    print(musician)

