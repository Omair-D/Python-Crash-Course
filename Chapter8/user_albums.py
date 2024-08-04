def make_album(artist, title, tracks = 0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

userTitle = '\nWhat is the album? '
userArtist = 'Who is the artist? '
print("Enter 'q' to quit at any time ")

while True:
    title = input(userTitle)
    if title == 'q':
        break
    
    artist = input(userArtist)
    if artist == 'q':
        break
    
    album = make_album(artist, title)
    print(album)

print("Thank you for your input!")