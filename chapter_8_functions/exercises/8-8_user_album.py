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

print("\nTell me about your favorite music! ")
print("(or type q to quit)")

while True: 

    artist = input("\nEnter an artist: ")
    
    if artist == 'q':
        break
    
    title = input(f"\n What's your favorite album from {artist}? ")
    
    if title == 'q': #redundant is break is avail at artist
        break

    formatted_music = make_album(artist, title)
    print(formatted_music)