'''
Write a function called make_album() that builds a dictionary
describing a music album. 

The function should take in an artist name and an album title, 
and it should return a dictionary containing these two pieces of information. 

Use the function to make three dictionaries representing different albums. 

Print each return value to show that the dictionaries are storing 
the album information correctly. 

'''

def make_album(artist, title):
    album_info = {'artist': artist.title(), 'title': title.capitalize()}
    return album_info


fav_music = make_album('the shins', 'oh inverted world')
print(fav_music)

fav_music = make_album('peach pit', 'peach pit')
print(fav_music)

fav_music = make_album('the wiggles', "I honestly don't know")
print(fav_music)